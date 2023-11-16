from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .uploads import S3ImgUploader
from .models import Playlist, Music
from user.models import User, Profile, Follower
from .youtube import YouTube
import os
import requests

# Create your views here.
class PlayList(APIView):
    def get(self, request):
        keyword = request.data['keyword']
        page  = request.GET.get("page")
        limit   = int(request.GET.get("limit", 1))
        youtube_instance = YouTube(keyword, page, limit)
        response_data = youtube_instance.youtube()
        print(response_data)
        return Response(response_data)
        # playlists = Playlist.objects.all(is_active=True)
        # for playlist in playlists:
        #     profile = Profile.objects.get(user=playlist.writer)
            
        


class Create(APIView):
    def post(self, request):
        pass


class Detail(APIView):
    def get(self, request, pk):
        pass


class Delete(APIView):
    def delete(self, reqeust):
        pass