from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiParameter, inline_serializer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.db.models import Count, Avg, Min, Max, Sum, Q
from django.shortcuts import get_object_or_404
from user.models import User, Profile
from user.serializers import ProfileSerializer
from .serializers import MusicSerializer, PlaylistSerializer, CommentSerializer
from .youtube import YouTube
from .karlo import t2i
from .gpt import get_music_recommendation, event_music_recommendation
from .playlist_utill import PlaylistAdder, PlaylistOrderUpdater, PlaylistRemover
from .uploads import S3ImgUploader
from .models import Playlist, Music, PlaylistMusic, Comment, Like
import json
import random

User = get_user_model()

# Create your views here.

class RandomMovieView(APIView):
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="랜덤 뮤비 조회 API",  # summary : 해당 method 요약
        description="랜덤 뮤비를 불러오는 API 입니다.",  # description: 해당 method 설명
        tags=["Random Movie"],  # tags : 문서상 보여줄 묶음의 단위
        responses=MusicSerializer,
        request=inline_serializer(
            name="Random_Movie_Play",
            fields={
                "already_musiclist": serializers.ListField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": [
                        {
                            "id": 14,
                            "song": "Snowman",
                            "singer": "Sia",
                            "thumbnail": "https://i.ytimg.com/vi/gset79KMmt0/mqdefault.jpg",
                            "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                            "created_at": "2023-08-24T10:01:38",
                        },{
                            "id": 7,
                            "song": "Snow",
                            "singer": "Red Hot Chili Peppers",
                            "thumbnail": "https://i.ytimg.com/vi/yuFI5KSPAt4/mqdefault.jpg",
                            "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                            "created_at": "2023-08-24T10:01:38",
                        },{
                            "id": 15,
                            "song": "Winter Song",
                            "singer": "Sara Bareilles",
                            "thumbnail": "https://i.ytimg.com/vi/budTp-4BGM0/mqdefault.jpg",
                            "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                            "created_at": "2023-08-24T10:01:38",}
                        ]},
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {"error": "Error Message"}},
            ),
        ],
    )
    def post(self, request):
        try:
            max_id = Music.objects.all().aggregate(max_id=Max("id"))['max_id'] # id Max 값 가져오기
            all_musiclist = [i for i in range(1,max_id+1)] # 모든 뮤직 리스트
            already_musiclist = [4,5,6] # 이미 본 리스트들
            # already_musiclist = request.data.get('already_musiclist')
            result = list(set(all_musiclist) - set(already_musiclist)) # 리스트 차집합
            
            random_musics = random.sample(result,3) # 랜덤 3개 뽑기
            queryset = Music.objects.filter(id__in=random_musics) # 해당 리스트를 검색
            # queryset = Music.objects.exclude(id__in=random_musics) # exclud 해당 리스트를 제외하고 검색

            serializer = MusicSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        
class EventPlaylistGenerate(APIView):
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="이벤트성 플레이리스트 생성 기능",
        description="이벤트성으로 한 문장으로 플레이리스트 생성 기능에 대한 API 입니다.",
        tags=["Event Playlist Generate"],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Event_Playlist_Generate",
            fields={
                "situations": serializers.CharField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "음악 생성 성공하였습니다"},
                },
            ),
        ],
    )
    def post(self, request):
        # 봉수님 코드 참고
        user = 'admin@admin.com'
        user = User.objects.get(email = user)
        genres = user.genre
        genres_list = genres.split(',')
        
        situations = request.data['situations'] # 현재 기분이나 상황
        genre = random.sample(genres_list,1) # 유저의 프로필에서 장르 랜덤으로 가져오기 
        response_data = event_music_recommendation(situations, genre)
        
        # is_public은 현우님이 정하시면 됩니다! 추가할지 안할지
        is_public = request.data['public']
        
        playlists = response_data['playlist']
        title = response_data['title']
        prompt = response_data['prompt']
        explanation = response_data['explanation']
        
        karlo = t2i(prompt)
        youtube_api = []
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title, thumbnail=karlo, genre=genre, is_public = is_public, content=explanation)
        music_list = []
        for playlist in playlists:
            # song, singer = map(str.strip, playlist.split(' - '))
            song, singer = playlist['song'], playlist['singer']
            keyword = f'{song} - {singer}'
            page = None
            limit = 1
            youtube_instance = YouTube(keyword, page, limit)
            youtube_data = youtube_instance.youtube()
            link_url = youtube_data['message'][0]['link_url']
            thumbnail = youtube_data['message'][0]['image_url']
            youtube_data = {
                'information' : link_url,
                'song' : song,
                'singer' : singer,
                'thumbnail' : thumbnail,
            }
            musicserializer = MusicSerializer(data = youtube_data)
            youtube_api.append(youtube_data)
            if musicserializer.is_valid():
                if not Music.objects.filter(singer__iexact=singer, song__iexact=song).exists():
                    music_instance = musicserializer.save()
                    music_list.append(music_instance)
                else:
                    exist_music = Music.objects.filter(singer=singer, song=song).first()
                    music_list.append(exist_music)
            else:
                return Response(musicserializer.errors)
        for order, music_instance in enumerate(music_list, start=1):
            PlaylistMusic.objects.create(
                playlist=playlist_instance,
                music=music_instance,
                order=order
            )
        # if created:
        #     # playlist_instance.music.add(*music_list)
        #     # playlist_instance.playlistmusic_set.add(*PlaylistMusic.objects.filter(playlist=playlist_instance))
        return Response({"message":"음악 생성 성공하였습니다"}, status=status.HTTP_200_OK)

# Create your views here.
class List(APIView):
    # permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="플레이리스트 메인 화면",
        description="플레이리스트 메인 화면에 대한 API 입니다.",
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"playlist_all":['objects'],"my_playlist":['objects'],"recommend_pli":['objects']},
                },
            ),
        ],
    )
    def get(self, request):
        
        ## 최신플리
        playlist_all = Playlist.objects.order_by('-created_at')[:5]
        recent_serializer = PlaylistSerializer(playlist_all, many=True).data
        ## 내가 만든 플리 
        user = request.user
        if user:
            user = User.objects.get(email = user).id
            playlist_mine = Playlist.objects.filter(writer=user)[:3]
            mine_serializer = PlaylistSerializer(playlist_mine, many=True).data
        
        ## 나를 위한 추천
            most_common_genre = Playlist.objects.filter(writer=user).values('genre').annotate(genre_count=Count('genre')).order_by('-genre_count').first()
            if most_common_genre:
                most_genre = most_common_genre['genre']
            
                recommend_playlist = Playlist.objects.filter(genre=most_genre).order_by('?')[:3]
                recommend_serializer = PlaylistSerializer(recommend_playlist, many=True).data
            else:
                recommend_serializer = ''
        else:
            mine_serializer = ''
            recommend_serializer = ''

        ## 핫한 플리(좋아요 많은 순)
        most_liked_playlists = Playlist.objects.annotate(count_like=Count('like')).order_by('-count_like')
        liked_serializer = PlaylistSerializer(most_liked_playlists, many=True).data[:3]
        
        mudig_playlist = {
            'playlist_all' : recent_serializer,
            'my_playlist' : mine_serializer,
            'recommend_pli' : recommend_serializer,
            'liked_playlist' : liked_serializer
        }
        
        return Response(mudig_playlist, status=status.HTTP_200_OK)


class Create(APIView):
    # permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="플레이리스트 생성 API",
        description="플레이리스트 생성에 대한 API 입니다.",
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Create",
            fields={
                "situations": serializers.CharField(),
                "genre": serializers.CharField(),
                "year": serializers.CharField()
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "음악 생성 성공하였습니다"},
                },
            ),
        ],
    )
    def post(self, request):
        # user = request.user
        user = 'admin@admin.com'
        user = User.objects.get(email=user)
        
        situations = request.data['situations']
        genre = request.data['genre']
        year = request.data['year']
        is_public = request.data['public']
        
        response_data = get_music_recommendation(situations, genre, year)
        
        playlists = response_data['playlist']
        title = response_data['title']
        prompt = response_data['prompt']
        explanation = response_data['explanation']
        
        
        karlo = t2i(prompt)
        youtube_api = []
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title, thumbnail=karlo, genre=genre, is_public = is_public, content=explanation)
        music_list = []
        for playlist in playlists:
            # song, singer = map(str.strip, playlist.split(' - '))
            song, singer = playlist['song'], playlist['singer']
            keyword = f'{song} - {singer}'
            page = None
            limit = 1
            print(song, singer)
            existing_music = Music.objects.filter(singer__iexact=singer, song__iexact=song).first()
            
            if existing_music:
                link_url = existing_music.information
                thumbnail = existing_music.thumbnail
            else:
                youtube_instance = YouTube(keyword, page, limit)
                youtube_data = youtube_instance.youtube()
                link_url = youtube_data['message'][0]['link_url']
                thumbnail = youtube_data['message'][0]['image_url']
            youtube_data = {
                'information' : link_url,
                'song' : song,
                'singer' : singer,
                'thumbnail' : thumbnail,
            }
            musicserializer = MusicSerializer(data = youtube_data)
            youtube_api.append(youtube_data)
            if musicserializer.is_valid():
                if not Music.objects.filter(singer__iexact=singer, song__iexact=song).exists():
                    music_instance = musicserializer.save()
                    music_list.append(music_instance)
                else:
                    exist_music = Music.objects.filter(singer__iexact=singer, song__iexact=song).first()
                    music_list.append(exist_music)
            else:
                return Response(musicserializer.errors)
        # print('music_list', music_list)
        for order, music_instance in enumerate(music_list, start=1):
            # print(music_instance)
            PlaylistMusic.objects.create(
                playlist=playlist_instance,
                music=music_instance,
                order=order
            )
        # if created:
        #     # playlist_instance.music.add(*music_list)
        #     # playlist_instance.playlistmusic_set.add(*PlaylistMusic.objects.filter(playlist=playlist_instance))
        return Response({"message":"음악 생성 성공하였습니다"}, status=status.HTTP_200_OK)


class Detail(APIView):
    # permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="플레이리스트 디테일 API",
        description="플레이리스트 디테일에 대한 API 입니다.",
        parameters=[],
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"playlist":['objects'],"music":['objects']},
                },
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {"error": "Error Message"},
                },
            ),
        ],
    )
    def get(self, request, pk):
        playlist_instance = get_object_or_404(Playlist, id=pk)

        # PlaylistMusic 모델을 통해 플레이리스트에 속한 음악들을 가져옵니다.

        ordered_music_instances = playlist_instance.playlistmusic_set.order_by('order').values_list('music', flat=True)
        music_instances = Music.objects.filter(pk__in=ordered_music_instances)
        music_dict = {music.id: music for music in music_instances}
        sorted_music_instances = [music_dict[music_id] for music_id in ordered_music_instances]
        
        music_serializer = MusicSerializer(sorted_music_instances, many=True)
        playlist_serializer = PlaylistSerializer(playlist_instance)
        user = Profile.objects.get(user = playlist_serializer.data['writer'])
        profile = ProfileSerializer(user)
        comment = Comment.objects.filter(playlist=playlist_instance)
        commentserializer = CommentSerializer(comment, many=True)
        comment = {
            'comment' : commentserializer.data,
            
        }
        data = {
            'user' : profile.data,
            'comments' : commentserializer.data,
            'playlist': playlist_serializer.data,
            'music': music_serializer.data,
            
        }

        return Response(data, status=status.HTTP_200_OK)


class Delete(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 삭제 API",
        description="플레이리스트 삭제에 대한 API 입니다.",
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Delete",
            fields={
                "playlist_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "플레이리스트 삭제 완료","playlist": bool,}
                },
            ),
        ],
    )
    def delete(self, request):
        playlist = Playlist.objects.get(id=request.data['playlist_id'])
        delete_img = S3ImgUploader(playlist.thumbnail)
        delete_img.delete()
        playlist.delete()
        # playlist.is_active = False
        # playlist.save()
        data = {
            "message" : "플레이리스트 삭제 완료",
            "playlist" : playlist.is_active
        }
        return Response(data, status=status.HTTP_200_OK)


class Update(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 수정 API",
        description="플레이리스트 수정에 대한 API 입니다.",
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Update",
            fields={
                "del_music_list": serializers.ListField(),
                "add_music_list": serializers.ListField(),
                "move_music": serializers.ListField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "수정완료"},
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {"error": "Error Message"},
                },
            ),
        ],
    )
    def put(self, request, pk):
        choice_playlist = Playlist.objects.get(id=pk)
        ## del music
        del_music_list_str = request.data.get('del_music_list', '')
        ## 언제든지 수정가능
        del_music_list = [int(item) for item in del_music_list_str.split(',') if item]
        if del_music_list:
            remove = PlaylistRemover()
            remove.remove_music(choice_playlist, del_music_list)
        
        ## add music
        add_music_list_str = request.data.get('add_music_list', '')
        add_music_list = [int(item) for item in add_music_list_str.split(',') if item]
        if add_music_list:
            add = PlaylistAdder()
            add.add_music(choice_playlist, add_music_list)
        
        ## move order
        move_music_list_str = request.data.get('move_music', '')
        # 입력 예제 6,5,4,3,2,1 임의로 정함 
        move_music_list = [int(item) for item in move_music_list_str.split(',') if item]
        if move_music_list_str:
            # move_music_list = json.loads(move_music_list_str)
            move = PlaylistOrderUpdater()
            move.update_order(choice_playlist, move_music_list)
        
        serializer = PlaylistSerializer(choice_playlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        ## order music
            data = {
                'message' : '수정완료',
                "message" : serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Add(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트에 음악 추가 API",
        description="플레이리스트에 특정 음악을 추가할 수 있는 기능에 대한 API 입니다.",
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Add",
            fields={
                "playlist_id": serializers.IntegerField(),
                "music": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "음악 이동 성공하였습니다"},
                },
            ),
        ],
    )
    def put(self, request):
        # pass
        playlist = Playlist.objects.get(id=request.data['playlist_id'])
        # music_list = request.data['music']
        music_list = list(map(int, request.data['music'].split(',')))
        music_add = PlaylistAdder()
        music_add.add_music(playlist, music_list)
        # max_order = (
        #     PlaylistMusic.objects.filter(playlist=playlist)
        #     .aggregate(models.Max('order'))['order__max'] or 0
        # )
        
        # # 테스트1
        # for order, music_id in enumerate(music_list, start=max_order):
        #     music = Music.objects.get(id=music_id)
        #     exist_music = PlaylistMusic.objects.filter(playlist=playlist, music_id=music)
        #     if exist_music:
        #         return Response({"message":"이미 플리안에 들어있는 노래입니다."}, status = status.HTTP_400_BAD_REQUEST)
        #     else:
        #         PlaylistMusic.objects.create(playlist=playlist, music=music, order= order + 1)

        # # add_music = playlist.music.add(*music_list)
        
        # music_objects = playlist.music.all()
        # print(music_objects)
        return Response({"message":"음악 이동 성공하였습니다"}, status=status.HTTP_200_OK)


## 내 플리 리스트 클래스
class MyPlaylist(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="내 플레이리스트 목록 API",
        description="내 플레이리스트를 보내주는 기능에 대한 API 입니다.",
        tags=["MyPlaylist"],
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"myplaylist": ['objects']},
                },
            ),
        ],
    )
    def get(self, request):
        user = request.user
        my_playlist = Playlist.objects.filter(writer = user.id)
        serializer = PlaylistSerializer()
        my_playlist_serializer = serializer.get_playlist_info(my_playlist)
        data = {
            'myplaylist': my_playlist_serializer
        }
        return Response(data, status=status.HTTP_200_OK)


class Allmusiclist(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="모든 음악 목록 API",
        description="모든 음악 목록을 보내주는 기능에 대한 API 입니다.",
        parameters=[],
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"music": ['objects']}
                },
            ),
        ],
    )
    def get(self, request):
        music = Music.objects.all()
        serializer = MusicSerializer()
        all_music = serializer.get_music_info(music)
        data = {
            'music' : all_music
        }
        return Response(data, status=status.HTTP_200_OK)


class SearchMusic(APIView):
    def get(self, request):
        query = request.data.get('query', None)
        print(query)
        if query == '':
            return Response({"message":"검색 창이 입력되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            music = Music.objects.filter(
                Q(song__contains=query)|
                Q(singer__contains=query)
            )
        musicserializer = MusicSerializer(music, many=True)
        if musicserializer.data != []:
            data = {
                "music_count" : len(musicserializer.data),
                "music" : musicserializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "검색한 해당 뮤직이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        


class Search(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 검색 API",
        description="플레이리스트를 검색하여 결과를 보내주는 기능에 대한 API 입니다.",
        tags=["Search"],
        parameters=[
            OpenApiParameter(
                name="query",
                type=str,
                description="검색할 단어",
                required=True,
            )],
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "recent_user":['objects'],
                        "recent_playlist":['objects'],
                        "users":['objects'],
                        "playlists":['objects'],
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": "Missing 'query' parameter",
                    }
                },
            ),
        ],
    )
    def get(self, request):
        query = request.GET.get('query')

        if not query:
            return Response({"error": "Missing 'query' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        users = Profile.objects.filter(Q(name__icontains=query) | Q(about__icontains=query)).order_by('-id')
        profile_serializer = ProfileSerializer(users, many=True).data

        recent_user = Profile.objects.filter(Q(name__icontains=query) | Q(about__icontains=query)).order_by('-id')[:3]
        recent_profile_serializer = ProfileSerializer(recent_user, many=True).data

        playlists = Playlist.objects.filter(Q(title__icontains=query)).order_by('-created_at')
        playlist_serializer = PlaylistSerializer(playlists, many=True).data

        recent_playlist = Playlist.objects.filter(Q(title__icontains=query),is_active=True).order_by('-created_at')[:3]      
        recent_playlist_serializer = PlaylistSerializer(recent_playlist, many=True).data
        
        response_data = {
            "recent_user" : recent_profile_serializer,
            "recent_playlist" : recent_playlist_serializer,
            "users" : profile_serializer,
            "playlists" : playlist_serializer
        }

        return Response(response_data, status=status.HTTP_200_OK)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 좋아요/취소 API",
        description="특정 플레이리스트의 좋아요/취소에 대한 API 입니다.",
        tags=["Like"],
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Like",
            fields={
                "playlist_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="201_CREATED",
                value={
                    "status": 201,
                    "res_data": {
                        "message": "좋아요 성공했습니다.",
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "message": "좋아요가 취소되었습니다.",
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": "잘못된 접근입니다.",
                    }
                },
            ),
        ],
    )
    def post(self, request):
        user = request.user
        
        try:
            playlist = Playlist.objects.get(id=request.data['playlist_id'])
            like, created = Like.objects.get_or_create(playlist=playlist, user=user)
        except ObjectDoesNotExist:
            return Response({"error":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)

        if created:
            return Response({"message":"좋아요 성공했습니다."}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message":"좋아요가 취소되었습니다."}, status=status.HTTP_200_OK)


class RecommentWrite(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 답글 작성 API",
        description="플레이리스트 답글 작성에 대한 API 입니다.",
        tags=["Comment"],
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Recomment_Write",
            fields={
                "content": serializers.CharField(),
                "playlist_id": serializers.IntegerField(),
                "parent_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="201_CREATED",
                value={
                    "status": 201,
                    "res_data": {
                        "message": "답글 생성 완료되었습니다.",
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": "Error Message",
                    }
                },
            ),
        ],
    )
    def post(self, request):
        user = request.user

        data = {
            "writer": user.id, 
            "content": request.data['content'], 
            "playlist": request.data['playlist_id'], 
            "parent": request.data['parent_id']
        }

        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            datas = {
                "message" : "답글 생성 완료되었습니다.",
            }
            return Response(datas,status=status.HTTP_201_CREATED)
        else:
            errors = {
                "error": serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

class CommentWrite(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 댓글 작성 API",
        description="플레이리스트 댓글 작성에 대한 API 입니다.",
        tags=["Comment"],
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Comment_Write",
            fields={
                "content": serializers.CharField(),
                "playlist_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="201_CREATED",
                value={
                    "status": 201,
                    "res_data": {
                        "message": "댓글 생성 완료되었습니다.",
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": "Error Message",
                    }
                },
            ),
        ],
    )
    def post(self, request):
        user = request.user

        data = {
            "writer": user.id, 
            "content": request.data['content'], 
            "playlist": request.data['playlist_id'], 
            "parent": None
        }

        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            datas = {
                "message" : "댓글 생성 완료되었습니다.",
            }
            return Response(datas,status=status.HTTP_201_CREATED)
        else:
            errors = {
                "error": serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

class CommentDelete(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 댓글 삭제 API",
        description="플레이리스트 댓글 삭제에 대한 API 입니다.",
        tags=["Comment"],
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Comment_Delete",
            fields={
                "comment_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "message": "댓글 삭제 완료되었습니다.",
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": "잘못된 접근입니다.",
                    }
                },
            ),
        ],
    )
    def delete(self, request):
        user = request.user

        try:
            comment = Comment.objects.get(id=request.data['comment_id'], writer=user)
        except ObjectDoesNotExist:
            return Response({"error":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        comment.is_active = False # 논리적 삭제
        comment.save()

        datas = {
            "message" : "댓글 삭제 완료되었습니다."
        }
        return Response(datas, status=status.HTTP_200_OK)   


class CommentEdit(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="플레이리스트 댓글 수정 API",
        description="플레이리스트 댓글 수정에 대한 API 입니다.",
        tags=["Comment"],
        parameters=[],
        responses=PlaylistSerializer,
        request=inline_serializer(
            name="Playlist_Comment_Edit",
            fields={
                "comment_id": serializers.IntegerField(),
                "content": serializers.CharField()
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "message": "댓글 수정 완료되었습니다.",
                    }
                },
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": "잘못된 접근입니다.",
                    }
                },
            ),
        ],
    )
    def put(self, request):
        user = request.user

        try:
            comment = Comment.objects.get(id=request.data['comment_id'], writer=user)
        except ObjectDoesNotExist:
            return Response({"error":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        comment.content = request.data['content']
        comment.save()
        
        data = {
            "message" : "댓글 수정 완료되었습니다."
        }
        
        return Response(data, status=status.HTTP_200_OK)