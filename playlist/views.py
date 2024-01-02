from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiParameter, inline_serializer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.db.models import Count, Max, Q
from django.shortcuts import get_object_or_404
from user.models import User, Profile
from user.serializers import ProfileSearchSerializer
from .serializers import MusicSerializer, PlaylistSerializer, CommentSerializer
from .youtube import YouTube
from .karlo import t2i
from .gpt import get_music_recommendation, event_music_recommendation
from .playlist_utill import PlaylistAdder, PlaylistOrderUpdater, PlaylistRemover
from .uploads import S3ImgUploader
from .models import Playlist, Music, PlaylistMusic, Comment, Like
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
                            "created_at": "2023-08-24T10:01:38",},
                        {
                            "id": 16,
                            "song": "하루살이",
                            "singer": "장범준",
                            "thumbnail": "https://i.ytimg.com/vi/QV8D6P-NR4c/mqdefault.jpg",
                            "information": "https://www.youtube.com/embed/QV8D6P-NR4c",
                            "created_at": "2023-08-24T10:01:38",},
                        {
                            "id": 23,
                            "song": "Lemon",
                            "singer": "요네즈 켄시",
                            "thumbnail": "https://i.ytimg.com/vi/p0ku3_rK6dE/mqdefault.jpg",
                            "information": "https://www.youtube.com/embed/p0ku3_rK6dE",
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

            already_musiclist_str = request.data.get('already_musiclist')
            already_musiclist = [int(item) for item in already_musiclist_str.split(',') if item]
            
            result = list(set(all_musiclist) - set(already_musiclist)) # 리스트 차집합
            random_musics = random.sample(result,5) # 랜덤 5개 뽑기
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
                    "res_data": {
                        "message": "음악 생성 성공하였습니다.",
                        "playlist": {
                            "id": 49,
                            "like_count": 0,
                            "like_playlist": False,
                            "title": "따뜻한 크리스마스 분위기를 전해주는 인디 캐롤 플레이리스트",
                            "content": "위의 인디 캐롤 플레이리스트는 크리스마스 분위기에 어울리며 따뜻한 감성을 전달합니다. 슬로우한 멜로디와 소울풀한 가사로 따스한 휴일 분위기를 만끽하세요!",
                            "thumbnail": "karlo/d5f3464aa2ea11eeae840700a75bb434",
                            "genre": "인디",
                            "is_active": True,
                            "created_at": "2023-12-25T14:59:59.371921+09:00",
                            "updated_at": "2023-12-25T14:59:59.371941+09:00",
                            "is_public": True,
                            "writer": 27,
                            "music": [
                                172,
                                173,
                                174,
                                175,
                                176
                            ]
                        }
                    },
                },
            ),
        ],
    )
    def post(self, request):
        # 봉수님 코드 참고
        user = request.user
        genres = user.profile.genre
        genres_list = genres.split(',')
        
        situations = request.data['situations'] # 현재 기분이나 상황
        genre = random.sample(genres_list,1) # 유저의 프로필에서 장르 랜덤으로 가져오기 
        response_data = event_music_recommendation(situations, genre[0])
        
        playlists = response_data['playlist']
        title = response_data['title']
        prompt = response_data['prompt']
        explanation = response_data['explanation']
        
        karlo = t2i(prompt)
        youtube_api = []
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title, thumbnail=karlo, genre=genre[0], content=explanation)
        playlistserializer = PlaylistSerializer(playlist_instance)
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

        data = {
            "message" : "음악 생성 성공하였습니다.",
            "playlist" : playlistserializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

# Create your views here.
class List(APIView):
    permission_classes = [IsAuthenticated]
    
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
                    "res_data": {
                        "playlist_all": [
                            {
                                "id": 49,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "따뜻한 크리스마스 분위기를 전해주는 인디 캐롤 플레이리스트",
                                "content": "위의 인디 캐롤 플레이리스트는 크리스마스 분위기에 어울리며 따뜻한 감성을 전달합니다. 슬로우한 멜로디와 소울풀한 가사로 따스한 휴일 분위기를 만끽하세요!",
                                "thumbnail": "karlo/d5f3464aa2ea11eeae840700a75bb434",
                                "genre": "인디",
                                "is_active": True,
                                "created_at": "2023-12-25T14:59:59.371921+09:00",
                                "updated_at": "2023-12-25T14:59:59.371941+09:00",
                                "is_public": True,
                                "writer": 27,
                                "music": [
                                    172,
                                    173,
                                    174,
                                    175,
                                    176
                                ]
                            },
                            {
                                "id": 48,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "겨울의 따뜻한 국물을 감성적으로 느낄 수 있는 플레이리스트",
                                "content": "추운 날씨에 꼭 필요한 따뜻한 국물처럼 마음을 감싸주는 음악들입니다. K-POP 장르로 2010년대에 발매된 곡들이며, 조용하고 감성적인 분위기를 즐길 수 있습니다.",
                                "thumbnail": "karlo/560c9168a2de11eeae840700a75bb434",
                                "genre": "POP",
                                "is_active": True,
                                "created_at": "2023-12-25T13:30:30.814652+09:00",
                                "updated_at": "2023-12-25T13:30:30.814672+09:00",
                                "is_public": True,
                                "writer": 5,
                                "music": [
                                    18,
                                    168,
                                    169,
                                    170,
                                    171
                                ]
                            },
                            {
                                "id": 47,
                                "like_count": 1,
                                "like_playlist": False,
                                "title": "따뜻한 국물과 함께 즐기는 추억의 K-POP 플레이리스트",
                                "content": "이 플레이리스트는 추울 때 뜨끈한 국물과 어울리는 2010년대 K-POP 음악으로 구성되어 있습니다. 이 음악들은 따뜻한 감성과 추억을 자아내며, 함께 즐길 때 더욱 풍성한 시간이 되리라 생각합니다. 즐거운 듣기 시간 되세요!",
                                "thumbnail": "karlo/2dbb8d0aa16b11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-23T17:13:39.906007+09:00",
                                "updated_at": "2023-12-23T17:13:39.906026+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    18,
                                    164,
                                    165,
                                    166,
                                    167
                                ]
                            },
                            {
                                "id": 30,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "디즈니 매직을 느낄 수 있는 플레이리스트!",
                                "content": "디즈니 애니메이션의 고전 OST들로 구성된 이 플레이리스트는 디즈니의 매력과 감동을 느낄 수 있게 해줄 거예요. 마음 속으로 여정을 떠나보세요!",
                                "thumbnail": "karlo/2a4aefb0a08c11eeae840700a75bb434",
                                "genre": "POP,OST",
                                "is_active": True,
                                "created_at": "2023-12-22T14:37:16.346946+09:00",
                                "updated_at": "2023-12-22T14:37:34.317543+09:00",
                                "is_public": True,
                                "writer": 6,
                                "music": [
                                    107,
                                    108,
                                    109,
                                    110,
                                    111
                                ]
                            },
                            {
                                "id": 29,
                                "like_count": 1,
                                "like_playlist": False,
                                "title": "태연의 감성을 담은 플레이리스트",
                                "content": "태연의 감성적인 목소리로 장난기 넘치는 곡부터 감미로운 발라드까지, 다양한 면을 담은 플레이리스트입니다. 태연의 노래를 통해 여러분의 감성을 풀어보세요!",
                                "thumbnail": "karlo/1838f754a08c11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:36:46.034374+09:00",
                                "updated_at": "2023-12-22T14:37:19.160935+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    102,
                                    103,
                                    104,
                                    105,
                                    106,
                                    113,
                                    114
                                ]
                            }
                        ],
                        "my_playlist": [
                            {
                                "id": 49,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "따뜻한 크리스마스 분위기를 전해주는 인디 캐롤 플레이리스트",
                                "content": "위의 인디 캐롤 플레이리스트는 크리스마스 분위기에 어울리며 따뜻한 감성을 전달합니다. 슬로우한 멜로디와 소울풀한 가사로 따스한 휴일 분위기를 만끽하세요!",
                                "thumbnail": "karlo/d5f3464aa2ea11eeae840700a75bb434",
                                "genre": "인디",
                                "is_active": True,
                                "created_at": "2023-12-25T14:59:59.371921+09:00",
                                "updated_at": "2023-12-25T14:59:59.371941+09:00",
                                "is_public": True,
                                "writer": 27,
                                "music": [
                                    172,
                                    173,
                                    174,
                                    175,
                                    176
                                ]
                            }
                        ],
                        "recommend_pli": [
                            {
                                "id": 17,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "활기찬 스노보드 여행을 위한 추천 플레이리스트입니다!",
                                "content": "이 플레이리스트는 활기찬 스노보드 여행에 딱 어울리는 댄스 음악들로 구성되어 있습니다. 신나고 흥겨운 느낌의 곡들로 스노보드 타는 동안에 즐거운 시간을 보내실 수 있을 거에요! 즐거운 여행되세요!",
                                "thumbnail": "karlo/49073064a08a11eeae840700a75bb434",
                                "genre": "댄스",
                                "is_active": True,
                                "created_at": "2023-12-22T14:23:48.894979+09:00",
                                "updated_at": "2023-12-22T14:24:15.907581+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    25,
                                    28,
                                    40,
                                    41,
                                    69
                                ]
                            },
                            {
                                "id": 22,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "아이유의 아름다운 음악들",
                                "content": "아이유의 감성적이고 따뜻한 음악들을 소개합니다. 이 플레이리스트를 들으면 마음이 편안해지고 기분 좋아질 것입니다. 아이유의 다양한 매력을 느껴보세요!",
                                "thumbnail": "karlo/27825f76a08b11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:30:02.194034+09:00",
                                "updated_at": "2023-12-22T14:30:28.193796+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    37,
                                    51,
                                    80,
                                    81,
                                    82,
                                    83
                                ]
                            },
                            {
                                "id": 19,
                                "like_count": 1,
                                "like_playlist": False,
                                "title": "Dua Lipa",
                                "content": "이 플레이리스트는 Dua Lipa의 인기곡들로 구성되어 있습니다. 신나고 흥겨운 노래들로 에너지를 얻을 수 있을 것입니다. 행복한 시간을 보내세요!",
                                "thumbnail": "karlo/706a3228a08a11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:24:54.978621+09:00",
                                "updated_at": "2023-12-22T14:31:41.997870+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    28,
                                    75,
                                    76,
                                    77,
                                    78
                                ]
                            },
                            {
                                "id": 16,
                                "like_count": 2,
                                "like_playlist": False,
                                "title": "아이묭의 아름다운 음악 여정",
                                "content": "이 플레이리스트는 2017년부터 현재까지의 아이묭의 감성적인 음악을 담고 있습니다. 아이묭의 일렉트로닉 사운드와 인디 감성이 어우러져 여러분의 마음을 흔들 것입니다. 편안하게 즐기세요!",
                                "thumbnail": "karlo/41e76376a08a11eeae840700a75bb434",
                                "genre": "J-POP,인디,POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:23:36.961757+09:00",
                                "updated_at": "2023-12-22T14:30:35.522247+09:00",
                                "is_public": True,
                                "writer": 6,
                                "music": [
                                    64,
                                    65,
                                    66,
                                    67,
                                    68
                                ]
                            },
                            {
                                "id": 9,
                                "like_count": 0,
                                "like_playlist": False,
                                "title": "창의적인 디자인을 위한 활력 넘치는 플레이리스트",
                                "content": "위 플레이리스트에는 디자인 회의에 참여하는 동안 에너지를 높여줄 댄스 음악들이 포함되어 있습니다. 이 음악들은 활발하면서도 긍정적인 분위기를 조성하며, 창의적인 아이디어 발굴을 도와줄 것입니다.",
                                "thumbnail": "karlo/ab9ba360a08811eeae840700a75bb434",
                                "genre": "댄스",
                                "is_active": True,
                                "created_at": "2023-12-22T14:12:15.360070+09:00",
                                "updated_at": "2023-12-22T14:20:34.330343+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    25,
                                    39,
                                    40,
                                    41,
                                    42,
                                    121
                                ]
                            }
                        ],
                        "liked_playlist": [
                            {
                                "id": 21,
                                "like_count": 2,
                                "like_playlist": False,
                                "title": "요네즈 켄시 노래 모음",
                                "content": "요네즈 켄시 노래 모음집입니다~",
                                "thumbnail": "karlo/9c48a79ea08a11eeae840700a75bb434",
                                "genre": "J-POP,인디",
                                "is_active": True,
                                "created_at": "2023-12-22T14:26:08.593904+09:00",
                                "updated_at": "2023-12-22T14:28:43.740870+09:00",
                                "is_public": True,
                                "writer": 6,
                                "music": [
                                    70,
                                    71,
                                    72,
                                    73
                                ]
                            },
                            {
                                "id": 16,
                                "like_count": 2,
                                "like_playlist": False,
                                "title": "아이묭의 아름다운 음악 여정",
                                "content": "이 플레이리스트는 2017년부터 현재까지의 아이묭의 감성적인 음악을 담고 있습니다. 아이묭의 일렉트로닉 사운드와 인디 감성이 어우러져 여러분의 마음을 흔들 것입니다. 편안하게 즐기세요!",
                                "thumbnail": "karlo/41e76376a08a11eeae840700a75bb434",
                                "genre": "J-POP,인디,POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:23:36.961757+09:00",
                                "updated_at": "2023-12-22T14:30:35.522247+09:00",
                                "is_public": True,
                                "writer": 6,
                                "music": [
                                    64,
                                    65,
                                    66,
                                    67,
                                    68
                                ]
                            },
                            {
                                "id": 19,
                                "like_count": 1,
                                "like_playlist": False,
                                "title": "Dua Lipa",
                                "content": "이 플레이리스트는 Dua Lipa의 인기곡들로 구성되어 있습니다. 신나고 흥겨운 노래들로 에너지를 얻을 수 있을 것입니다. 행복한 시간을 보내세요!",
                                "thumbnail": "karlo/706a3228a08a11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:24:54.978621+09:00",
                                "updated_at": "2023-12-22T14:31:41.997870+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    28,
                                    75,
                                    76,
                                    77,
                                    78
                                ]
                            },
                            {
                                "id": 47,
                                "like_count": 1,
                                "like_playlist": False,
                                "title": "따뜻한 국물과 함께 즐기는 추억의 K-POP 플레이리스트",
                                "content": "이 플레이리스트는 추울 때 뜨끈한 국물과 어울리는 2010년대 K-POP 음악으로 구성되어 있습니다. 이 음악들은 따뜻한 감성과 추억을 자아내며, 함께 즐길 때 더욱 풍성한 시간이 되리라 생각합니다. 즐거운 듣기 시간 되세요!",
                                "thumbnail": "karlo/2dbb8d0aa16b11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-23T17:13:39.906007+09:00",
                                "updated_at": "2023-12-23T17:13:39.906026+09:00",
                                "is_public": True,
                                "writer": 7,
                                "music": [
                                    18,
                                    164,
                                    165,
                                    166,
                                    167
                                ]
                            },
                            {
                                "id": 23,
                                "like_count": 1,
                                "like_playlist": False,
                                "title": "KPOP 여자 아이돌의 활력 넘치는 노래모음",
                                "content": "이 플레이리스트는 2020년부터 현재까지의 인기 K-POP 여자 아이돌의 활력 넘치는 노래들로 구성되어 있습니다. 업텐션과 흥미를 주는 리듬과 강렬한 보컬로 여러분의 기분을 업그레이드해줄 것입니다. 즐겁게 감상하세요!",
                                "thumbnail": "karlo/6c74aaf8a08b11eeae840700a75bb434",
                                "genre": "K-POP",
                                "is_active": True,
                                "created_at": "2023-12-22T14:31:57.895432+09:00",
                                "updated_at": "2023-12-22T14:35:53.256432+09:00",
                                "is_public": True,
                                "writer": 6,
                                "music": [
                                    15,
                                    84,
                                    85,
                                    86,
                                    87
                                ]
                            }
                        ]
                        },
                },
            ),
        ],
    )
    def get(self, request):
        
        ## 최신플리
        playlist_all = Playlist.objects.filter(is_public=True).order_by('-created_at')[:5]
        recent_serializer = PlaylistSerializer(playlist_all, many=True).data
        ## 내가 만든 플리 
        user = request.user
        if user:
            user = User.objects.get(email = user).id
            playlist_mine = Playlist.objects.filter(writer=user).order_by('-created_at')[:4]
            mine_serializer = PlaylistSerializer(playlist_mine, many=True).data
            most_common_genre = []
            ## 나를 위한 추천
            # 'POP, K-POP, J-POP, 힙합, R&B, 발라드, 댄스, 인디, OST' 
            profile = Profile.objects.get(user=user)
            profile_genre = list(profile.genre.split(',')) if profile.genre else []
            try:
                while not most_common_genre:
                    selected_genre = random.choice(profile_genre)
                    profile_genre.remove(selected_genre)
                    most_common_genre = Playlist.objects.filter(genre=selected_genre, is_public=True).exclude(writer=user).order_by('?')[:5]
                    selected_genre = []
            except IndexError:
                most_common_genre = Playlist.objects.filter(is_public=True).exclude(writer=user).order_by('?')[:5]
            if most_common_genre:
                recommend_serializer = PlaylistSerializer(most_common_genre, many=True).data
            else:
                recommend_serializer = []
        else:
            mine_serializer = []
            recommend_serializer = []

        ## 핫한 플리(좋아요 많은 순)
        most_liked_playlists = Playlist.objects.filter(is_public=True).annotate(count_like=Count('like')).order_by('-count_like')
        liked_serializer = PlaylistSerializer(most_liked_playlists, many=True).data[:5]
        
        mudig_playlist = {
            'playlist_all' : recent_serializer,
            'my_playlist' : mine_serializer,
            'recommend_pli' : recommend_serializer,
            'liked_playlist' : liked_serializer
        }
        
        return Response(mudig_playlist, status=status.HTTP_200_OK)


class Create(APIView):
    permission_classes = [IsAuthenticated]
    
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
                    "res_data": {
                        "message": "음악 생성 성공하였습니다.",
                        "playlist": {
                            "id": 7,
                            "like_count": 0,
                            "title": "눈이 내리는 날을 위한 우울하지 않은 노래들",
                            "content": "이 노래들은 눈이 내리는 날의 분위기에 잘 어울리며 우울하지 않은 톤으로 겨울을 즐기는 느낌을 전해줍니다. 이 플레이리스트를 통해 눈 오는 날의 풍경과 함께 편안한 시간을 보내세요!",
                            "thumbnail": "karlo/bda686f594f511eeacf3e0d464928253",
                            "genre": "pop",
                            "is_active": True,
                            "created_at": "2023-12-07T20:42:46.741054+09:00",
                            "updated_at": "2023-12-07T20:42:46.741054+09:00",
                            "is_public": False,
                            "writer": 1,
                            "music": [
                                11,
                                26,
                                27,
                                28,
                                14]}
                    }},
            ),
        ],
    )
    def post(self, request):
        user = request.user
        
        situations = request.data['situations']
        genre = request.data['genre']
        year = request.data['year']
        
        response_data = get_music_recommendation(situations, genre, year)
        
        playlists = response_data['playlist']
        title = response_data['title']
        prompt = response_data['prompt']
        explanation = response_data['explanation']
        
        
        karlo = t2i(prompt)
        youtube_api = []
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title, thumbnail=karlo, genre=genre, content=explanation)
        playlistserializer = PlaylistSerializer(playlist_instance)
        music_list = []
        for playlist in playlists:
            # song, singer = map(str.strip, playlist.split(' - '))
            song, singer = playlist['song'], playlist['singer']
            keyword = f'{song} - {singer}'
            page = None
            limit = 1
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
        for order, music_instance in enumerate(music_list, start=1):
            PlaylistMusic.objects.create(
                playlist=playlist_instance,
                music=music_instance,
                order=order
            )
        # if created:
        #     # playlist_instance.music.add(*music_list)
        #     # playlist_instance.playlistmusic_set.add(*PlaylistMusic.objects.filter(playlist=playlist_instance))
        music_serializer = MusicSerializer(music_list, many=True)
        data = {
            "message" : "음악 생성 성공하였습니다.",
            "playlist" : playlistserializer.data,
            "playlist_music_list": music_serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class Detail(APIView):
    permission_classes = [IsAuthenticated]
    
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
                    "res_data": {
                        "user": {
                            "id": 6,
                            "name": "FE_다얀",
                            "image": "profile/39bba74aa08d11eeae840700a75bb434",
                            "about": "Hi there",
                            "genre": "K-POP,J-POP,인디",
                            "email": "dayoun202@gmail.com",
                            "rep_playlist": 8
                        },
                        "comments": [],
                        "playlist": {
                            "id": 42,
                            "like_count": 0,
                            "like_playlist": False,
                            "title": "지브리 애니메이션 OST",
                            "content": "지브리 애니메이션 OST",
                            "thumbnail": "karlo/89d531e6a09d11eeae840700a75bb434",
                            "genre": "J-POP,OST",
                            "is_active": True,
                            "created_at": "2023-12-22T16:41:38.109400+09:00",
                            "updated_at": "2023-12-22T16:42:30.919304+09:00",
                            "is_public": False,
                            "writer": 6,
                            "music": [
                                148,
                                149,
                                150,
                                151
                            ]
                        },
                        "music": [
                            {
                                "id": 148,
                                "information": "https://www.youtube.com/embed/TK1Ij_-mank",
                                "singer": "Joe Hisaishi",
                                "song": "One Summer\"s Day",
                                "thumbnail": "https://i.ytimg.com/vi/TK1Ij_-mank/mqdefault.jpg",
                                "created_at": "2023-12-22T16:41:40.125103+09:00"
                            },
                            {
                                "id": 149,
                                "information": "https://www.youtube.com/embed/ze0-fv8QKA4",
                                "singer": "Joe Hisaishi",
                                "song": "Nausicaä of the Valley of the Wind",
                                "thumbnail": "https://i.ytimg.com/vi/ze0-fv8QKA4/mqdefault.jpg",
                                "created_at": "2023-12-22T16:41:41.344939+09:00"
                            },
                            {
                                "id": 150,
                                "information": "https://www.youtube.com/embed/ArR9jochJgU",
                                "singer": "Yae",
                                "song": "The Tatara Women Work Song",
                                "thumbnail": "https://i.ytimg.com/vi/ArR9jochJgU/mqdefault.jpg",
                                "created_at": "2023-12-22T16:41:42.239240+09:00"
                            },
                            {
                                "id": 151,
                                "information": "https://www.youtube.com/embed/evO35dDsSvA",
                                "singer": "Nozomi Ohashi",
                                "song": "Ponyo on the Cliff by the Sea",
                                "thumbnail": "https://i.ytimg.com/vi/evO35dDsSvA/mqdefault.jpg",
                                "created_at": "2023-12-22T16:41:43.185357+09:00"
                            }
                        ]    
                    },
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
    def get(self, request, playlist_id):
        playlist_instance = get_object_or_404(Playlist, id=playlist_id)
        # PlaylistMusic 모델을 통해 플레이리스트에 속한 음악들을 가져옵니다.

        ordered_music_instances = playlist_instance.playlistmusic_set.order_by('order').values_list('music', flat=True)
        music_instances = Music.objects.filter(pk__in=ordered_music_instances)
        music_dict = {music.id: music for music in music_instances}
        sorted_music_instances = [music_dict[music_id] for music_id in ordered_music_instances]
        
        music_serializer = MusicSerializer(sorted_music_instances, many=True)
        playlist_serializer = PlaylistSerializer(playlist_instance, context={'request': request})
        playlist_serializer.get_like_count(playlist_instance)
        user_like = playlist_serializer.get_like_playlist(playlist_instance)
        user = Profile.objects.get(user = playlist_serializer.data['writer'])
        profile = ProfileSearchSerializer(user)
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
    def delete(self, request, playlist_id):
        user = request.user
        try:
            playlist = Playlist.objects.get(id = playlist_id, writer = user)
        except ObjectDoesNotExist:
            return Response({"error":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        delete_img = S3ImgUploader(playlist.thumbnail)
        delete_img.delete()
        
        pli_id = playlist.id
        profile = user.profile
        rep_pli = profile.rep_playlist
        
        if rep_pli:
            if pli_id == rep_pli.id:
                profile.rep_playlist = None
                profile.save()

        playlist.delete()
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
                "del_music_list": serializers.CharField(),
                "add_music_list": serializers.CharField(),
                "move_music": serializers.CharField(),
                "title": serializers.CharField(),
                "content": serializers.CharField(),
                "is_public": serializers.BooleanField(),
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
    def put(self, request, playlist_id):
        user = request.user
        choice_playlist = Playlist.objects.get(id=playlist_id, writer=user)
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
            
            public = serializer.validated_data.get('is_public')
            pli_id = serializer.instance.id
            profile = user.profile
            rep_pli = profile.rep_playlist
            
            if rep_pli:
                if not public:
                    if pli_id == rep_pli.id:
                        profile.rep_playlist = None
                        profile.save()
            
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

        user = request.user
        playlist = Playlist.objects.get(id=request.data['playlist_id'], writer = user)

        music_list = list(map(int, request.data['music'].split(',')))
        music_add = PlaylistAdder()
        music_add.add_music(playlist, music_list)
        
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
                    "res_data": {"myplaylist": [
                                    {
                                        "id": 49,
                                        "thumbnail": "karlo/d5f3464aa2ea11eeae840700a75bb434",
                                        "title": "따뜻한 크리스마스 분위기를 전해주는 인디 캐롤 플레이리스트"
                                    }
                                ]},
                },
            ),
        ],
    )
    def get(self, request):
        user = request.user
        my_playlist = Playlist.objects.filter(writer=user.id,is_public=True,is_active=True)
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
                        "recent_users": [
                            {
                                "id": 30,
                                "name": "mudig05",
                                "image": "profile/basic.png",
                                "about": "음악을 좋아합니다",
                                "genre": "K-POP,J-POP",
                                "email": "mudig015@gmail.com",
                                "rep_playlist": None
                            },
                        ],
                        "recent_playlists": [
                            {
                                "playlist": {
                                    "id": 49,
                                    "like_count": 0,
                                    "like_playlist": False,
                                    "title": "따뜻한 크리스마스 분위기를 전해주는 인디 캐롤 플레이리스트",
                                    "content": "위의 인디 캐롤 플레이리스트는 크리스마스 분위기에 어울리며 따뜻한 감성을 전달합니다. 슬로우한 멜로디와 소울풀한 가사로 따스한 휴일 분위기를 만끽하세요!",
                                    "thumbnail": "karlo/d5f3464aa2ea11eeae840700a75bb434",
                                    "genre": "인디",
                                    "is_active": True,
                                    "created_at": "2023-12-25T14:59:59.371921+09:00",
                                    "updated_at": "2023-12-25T14:59:59.371941+09:00",
                                    "is_public": True,
                                    "writer": 27,
                                    "music": [
                                        172,
                                        173,
                                        174,
                                        175,
                                        176
                                    ]
                                },
                                "writer": {
                                    "id": 27,
                                    "name": "mudig02",
                                    "image": "profile/basic.png",
                                    "about": "안녕",
                                    "genre": "힙합,인디,OST",
                                    "email": "mudig012@email.com",
                                    "rep_playlist": None
                                }
                            },],
                        "users": [
                            {"id": 29,
                            "name": "mudig04",
                            "image": "profile/basic.png",
                            "about": "소개글을 작성해주세요.",
                            "genre": "힙합",
                            "email": "mudig014@gmail.com",
                            "rep_playlist": None,}
                            ],
                        "playlists": [
                            {
                                "playlist": {
                                    "id": 49,
                                    "like_count": 0,
                                    "like_playlist": False,
                                    "title": "따뜻한 크리스마스 분위기를 전해주는 인디 캐롤 플레이리스트",
                                    "content": "위의 인디 캐롤 플레이리스트는 크리스마스 분위기에 어울리며 따뜻한 감성을 전달합니다. 슬로우한 멜로디와 소울풀한 가사로 따스한 휴일 분위기를 만끽하세요!",
                                    "thumbnail": "karlo/d5f3464aa2ea11eeae840700a75bb434",
                                    "genre": "인디",
                                    "is_active": True,
                                    "created_at": "2023-12-25T14:59:59.371921+09:00",
                                    "updated_at": "2023-12-25T14:59:59.371941+09:00",
                                    "is_public": True,
                                    "writer": 27,
                                    "music": [
                                        172,
                                        173,
                                        174,
                                        175,
                                        176
                                    ]
                                },
                                "writer": {
                                    "id": 27,
                                    "name": "mudig02",
                                    "image": "profile/basic.png",
                                    "about": "안녕",
                                    "genre": "힙합,인디,OST",
                                    "email": "mudig012@email.com",
                                    "rep_playlist": None
                                }
                            },]
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

        users = Profile.objects.filter(Q(name__icontains=query) | Q(about__icontains=query),user__is_active=True).order_by('-id')
        profile_serializer = ProfileSearchSerializer(users, many=True).data

        recent_user = Profile.objects.filter(Q(name__icontains=query) | Q(about__icontains=query),user__is_active=True).order_by('-id')[:3]
        recent_profile_serializer = ProfileSearchSerializer(recent_user, many=True).data

        playlists = Playlist.objects.filter(Q(title__icontains=query)).order_by('-created_at')
        playlist_serializer = PlaylistSerializer(playlists, many=True).data

        search_playlist = []
        for p_s in playlist_serializer:
            try:
                writer = Profile.objects.get(id=p_s['writer'])
            except:
                writer_info = "유저 정보 없음"
            else:
                writer_info = ProfileSearchSerializer(writer).data
                
        
            playlist_info = {
                'playlist' : p_s,
                'writer' : writer_info
            }
            search_playlist.append(playlist_info)

        recent_playlists = Playlist.objects.filter(Q(title__icontains=query)).order_by('-created_at')[:3]
        recent_playlist_serializer = PlaylistSerializer(recent_playlists, many=True).data

        recent_search_playlist = [] 
        for recent_p_s in recent_playlist_serializer:
            try:
                recent_writer = Profile.objects.get(id=recent_p_s['writer'])
            except:
                recent_writer_info = "유저 정보 없음"
            else:
                recent_writer_info = ProfileSearchSerializer(recent_writer).data

            recent_playlist_info = {
                'playlist' : recent_p_s,
                'writer' : recent_writer_info
            }
            recent_search_playlist.append(recent_playlist_info)

        response_data = {
            "recent_users" : recent_profile_serializer,
            "recent_playlists" : recent_search_playlist,
            "users" : profile_serializer,
            "playlists" : search_playlist
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
    def delete(self, request, comment_id):
        user = request.user

        try:
            comment = Comment.objects.get(id=comment_id, writer=user)
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