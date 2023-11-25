from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from .uploads import S3ImgUploader
from .models import Playlist, Music, PlaylistMusic, Comment, Like
from user.models import User, Profile, Follower
from .serializers import MusicSerializer, PlaylistSerializer, CommentSerializer
from .youtube import YouTube
from .karlo import t2i
from .gpt import get_music_recommendation
from .playlist_utill import PlaylistAdder, PlaylistOrderUpdater, PlaylistRemover
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
import os
import requests
import json

# Create your views here.
class List(APIView):
    def get(self, request):
        
        ## 최신플리
        playlist_all = Playlist.objects.order_by('-created_at')[:5]
        recent_serializer = PlaylistSerializer(playlist_all, many=True).data
        ## 내가 만든 플리 
        # user = request.user
        user = 'admin@admin.com'
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
        
        
        mudig_playlist = {
            'playlist_all' : recent_serializer,
            'my_playlist' : mine_serializer,
            'recommend_pli' : recommend_serializer
        }
        
        return Response(mudig_playlist)


class Create(APIView):
    def post(self, request):
        ## user
        # user = request.user
        # user = User.objects.get(email=user)
        ##
        user = 'admin@admin.com'
        user = User.objects.get(email = user)
        
        situations = request.data['situations']
        genre = request.data['genre']
        year = request.data['year']
        response_data = get_music_recommendation(situations, genre, year)
        
        playlists = response_data['playlist']
        title = response_data['title']
        prompt = response_data['prompt']
        
        karlo = t2i(prompt)
        youtube_api = []
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title, thumbnail=karlo, genre=genre)
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

# test count 27


class Detail(APIView):
    def get(self, request, pk):
        playlist_instance = get_object_or_404(Playlist, id=pk)

        # PlaylistMusic 모델을 통해 플레이리스트에 속한 음악들을 가져옵니다.

        ordered_music_instances = playlist_instance.playlistmusic_set.order_by('order').values_list('music', flat=True)
        music_instances = Music.objects.filter(pk__in=ordered_music_instances)
        music_dict = {music.id: music for music in music_instances}
        sorted_music_instances = [music_dict[music_id] for music_id in ordered_music_instances]
        
        music_serializer = MusicSerializer(sorted_music_instances, many=True)
        playlist_serializer = PlaylistSerializer(playlist_instance)
        
        data = {
            'playlist': playlist_serializer.data,
            'music': music_serializer.data
        }

        
        return Response(data, status=status.HTTP_200_OK)
        # pass


class Delete(APIView):
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
        if move_music_list_str:
            move_music_list = json.loads(move_music_list_str)
            move = PlaylistOrderUpdater()
            move.update_order(choice_playlist, move_music_list)
            
        ## order music
        data = {
            'message' : '수정완료'
        }
        return Response(data, status=status.HTTP_200_OK)


class Add(APIView):
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
    def get(self, request):
        # user = request.user
        user = 'admin@admin.com'
        user = User.objects.get(email=user)
        my_playlist = Playlist.objects.filter(writer = user.id)
        serializer = PlaylistSerializer()
        my_playlist_serializer = serializer.get_playlist_info(my_playlist)
        data = {
            'myplaylist': my_playlist_serializer
        }
        return Response(data, status=status.HTTP_200_OK)


class Allmusiclist(APIView):
    def get(self, request):
        music = Music.objects.all()
        serializer = MusicSerializer()
        all_music = serializer.get_music_info(music)
        data = {
            'music' : all_music
        }
        return Response(data, status=status.HTTP_200_OK)


User = get_user_model()

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        
        try:
            playlist = Playlist.objects.get(id=request.data['playlist_id'])
            like, created = Like.objects.get_or_create(playlist=playlist, user=user)
        except ObjectDoesNotExist:
            return Response({"detail":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)

        if created:
            return Response({"detail":"좋아요 성공했습니다."}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"detail":"좋아요가 취소되었습니다."}, status=status.HTTP_200_OK)


class RecommentWrite(APIView):
    permission_classes = [IsAuthenticated]

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
                "detail" : "답글 생성 완료되었습니다.",
            }
            return Response(datas,status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

class CommentWrite(APIView):
    permission_classes = [IsAuthenticated]

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
                "detail" : "댓글 생성 완료되었습니다.",
            }
            return Response(datas,status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

class CommentDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user

        try:
            comment = Comment.objects.get(playlist=request.data['playlist_id'], id=request.data['comment_id'], writer=user)
        except ObjectDoesNotExist:
            return Response({"detail":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        # comment = Comment.objects.get(id=request.data['comment_id'])
        
        comment.is_active = False # 논리적 삭제
        comment.save()

        datas = {
            "detail" : "댓글 삭제 완료되었습니다."
        }
        return Response(datas, status=status.HTTP_200_OK)   


class CommentEdit(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user

        try:
            comment = Comment.objects.get(playlist=request.data['playlist_id'], id=request.data['comment_id'], writer=user)
        except ObjectDoesNotExist:
            return Response({"detail":"잘못된 접근입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        comment.content = request.data['content']
        comment.save()
        
        data = {
            "detail" : "댓글 수정 완료되었습니다."
        }
        
        return Response(data, status=status.HTTP_200_OK)
    

