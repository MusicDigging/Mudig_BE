from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .uploads import S3ImgUploader
from .models import Playlist, Music
from user.models import User, Profile, Follower
from .serializers import MusicSerializer, PlayListSerializer
from .youtube import YouTube
from .karlo import t2i
from .gpt import get_music_recommendation
import os
import requests
import json

# Create your views here.
class List(APIView):
    def get(self, request):
        
        ## 플리_전체
        playlist_all = Playlist.objects.all()
        print('playlist_all', playlist_all)
        all_serializer = PlayListSerializer(playlist_all, many=True)
        # print(all_serializer.data)
        ## 내가 만든 플리 
        user = 'admin@admin.com'
        # user = request.user
        user = User.objects.get(email = user).id
        # print(user.id)
        playlist_mine = Playlist.objects.filter(writer=user)
        mine_serializer = PlayListSerializer(playlist_mine, many=True)
        
        ## 나를 위한 추천
        
        ## 핫한 플리(좋아요 많은 순)
        
        
        mudig_playlist = {
            'playlist_all' : all_serializer.data[:5],
            'my_playlist' : mine_serializer.data
        }
        
        return Response(mudig_playlist)


class Create(APIView):
    def post(self, request):
        ## user
        # user = request.user
        # user = User.objects.get(username=user)
        ##
        user = 'admin@admin.com'
        user = User.objects.get(email = user)
        
        situatuons = request.data['situatuons']
        genre = request.data['genre']
        year = request.data['year']
        response_data = get_music_recommendation(situatuons, genre, year)
        print('data', response_data)
        response_json = json.loads(response_data.replace("'", "\""))
        response_json = response_json.replace("n\"t", "n\'t")
        print('json', response_json)
        playlists = response_json['playlist']
        title = response_json['title']
        prompt = response_json['prompt']
        karlo = t2i(prompt)
        playlists = playlists.split(',')
        # print('playlists', playlists)
        youtube_api = []
        # music_list = Music.objects.all()
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title, thumbnail=karlo)
        print(playlist_instance, created)
        music_list = []
        for playlist in playlists:
            print(playlist)
            song, singer = map(str.strip, playlist.split(' - '))
            keyword = playlist
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
                'genre': genre,
            }
            musicserializer = MusicSerializer(data = youtube_data)
            youtube_api.append(youtube_data)
            if musicserializer.is_valid():
                if not Music.objects.filter(singer=singer, song=song).exists():
                    music_instance = musicserializer.save()
                    print('if not Music.objects.filter(singer=singer, song=song).exists()',singer, song)
                    music_list.append(music_instance)
                else:
                    exist_music = Music.objects.filter(singer=singer, song=song).first()
                    music_list.append(exist_music)
                    
            else:
                return Response(musicserializer.errors)
        if created:
            playlist_instance.music.add(*music_list)
        return Response({"message":"음악 생성 성공하였습니다"}, status=status.HTTP_200_OK)

# test count 27


class Detail(APIView):
    def get(self, request, pk):
        playlist_choice = Playlist.objects.get(id=pk)
        # profile = User.objects.get(email=playlist_choice.writer)
        music_objects = playlist_choice.music.all()
        music_serializer = MusicSerializer(music_objects, many=True)
        # user_serializer = UserSerializer(User)
        data = {
            'music': music_serializer.data,
            # 'profile' :profile
        }
        return Response(data, status=status.HTTP_200_OK)
        # pass


class Delete(APIView):
    def delete(self, request):
        playlist = Playlist.objects.get(id=request.data['playlist_id'])
        print(playlist.thumbnail)
        delete_img = S3ImgUploader(playlist.thumbnail)
        delete_img.delete()
        # playlist.delete()
        # playlist.is_active = False
        # playlist.save()
        data = {
            "message" : "플레이리스트 삭제 완료",
            "playlist" : playlist.is_active
        }
        return Response(data, status=status.HTTP_200_OK)


class Update(APIView):
    def put(self, request, pk):
        pass


class Add(APIView):
    def put(self, request):
        # pass
        playlist = Playlist.objects.get(id=request.data['pli_id'])
        # music_list = request.data['music']
        music_list = list(map(int, request.data['music'].split(',')))
        # 테스트1
        # for music in music_list:
        #     add_music = Music.objects.get(id=music)
        #     add_music.save()
        
        add_music = playlist.music.add(*music_list)
        
        music_objects = playlist.music.all()
        # print(music_objects)
        return Response({"message":"음악 이동 성공하였습니다"}, status=status.HTTP_200_OK)

