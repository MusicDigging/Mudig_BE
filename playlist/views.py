from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .uploads import S3ImgUploader
from .models import Playlist, Music
from user.models import User, Profile, Follower
from .serializers import MusicSerializer, PlayListSerializer
from .youtube import YouTube
from .gpt import get_music_recommendation
import os
import requests
import json

# Create your views here.
class List(APIView):
    def get(self, request):
        # keyword = request.data['keyword']
        # page  = request.GET.get("page")
        # print(page)
        # limit   = int(request.GET.get("limit", 1))
        # print(limit)
        # youtube_instance = YouTube(keyword, page, limit)
        # response_data = youtube_instance.youtube()
        
        # print(response_data['message'][0]['image_url'])
        # a = response_data['message']
        # print(a['image_url'])
        # youtube_api = json.load(response_data)
        # image =  youtube_api['message']['image_url']
        # print(image)
        playlist_instance = Playlist.objects.get(pk=2)

# Access the 'music' field of the Playlist instance
        music_objects = playlist_instance.music.all()
        print(music_objects)
        for i in music_objects:
            print('qweqweqwe', i.sing)
        # print(response_data)
        return Response(music_objects)
        # pass
        # playlists = Playlist.objects.all(is_active=True)
        # for playlist in playlists:
        #     profile = Profile.objects.get(user=playlist.writer)
            
        


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
        # print(response_json['playlist'])
        playlists = response_json['playlist']
        title = response_json['title']
        prompt = response_json['prompt']
        playlists = playlists.split(',')
        # print('playlists', playlists)
        youtube_api = []
        # music_list = Music.objects.all()
        
        playlist_instance, created = Playlist.objects.get_or_create(writer=user, title=title)
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
                    'sing' : playlist,
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
# test count 15


class Detail(APIView):
    def get(self, request, pk):
        pass


class Delete(APIView):
    def delete(self, reqeust):
        pass