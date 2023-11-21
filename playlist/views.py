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
        feature = request.data['feature']
        year = request.data['year']
        response_data = get_music_recommendation(situatuons, feature, year)
        print('data', response_data)
        response_json = json.loads(response_data.replace("'", "\""))
        print('json', response_json)
        # try:
        #     response_json = json.loads(response_data.replace("'", "\""))
        #     # response_json = json.loads(response_data)
        #     print('json', response_json)
        # except json.decoder.JSONDecodeError as e:
        #     print('Error decoding JSON:', str(e))
        # print(response_json['playlist'])
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
            # song, singer = playlist.split(' - ')
            song, singer = map(str.strip, playlist.split(' - '))
            if not Music.objects.filter(singer=singer, song=song).exists():
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
                    'thumbnail' : thumbnail
                }
                musicserializer = MusicSerializer(data = youtube_data)
                youtube_api.append(youtube_data)
                if musicserializer.is_valid():
                    music_instance = musicserializer.save()
                    music_list.append(music_instance)
                else:
                    return Response(musicserializer.errors)
            else:
                continue
        # print(youtube_api)
        if created:
            playlist_instance.music.add(*music_list)
        return Response(youtube_api)
# test count 20


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
    def delete(self, reqeust, pk):
        playlist = Playlist.objects.get(id=pk)
        playlist.delete()
        # playlist.is_active = False
        # playlist.save()
        data = {
            "message" : "플레이리스트 삭제 완료",
            "playlist" : playlist.is_active
        }
        return Response(data, status=status.HTTP_200_OK)