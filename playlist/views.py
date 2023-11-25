from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q 
from .models import Playlist, Comment, Like
from user.models import Profile
from .serializers import PlaylistSerializer ,CommentSerializer
from user.serializers import ProfileSerializer
from rest_framework.views import APIView
# Create your views here.

User = get_user_model()

class Search(APIView):
    def get(self, request):
        query = request.GET.get('query') 

        if not query:
            return Response({"error": "Missing 'query' parameter"}, status=400)

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
    

