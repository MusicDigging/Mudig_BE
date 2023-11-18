from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Playlist, Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
# Create your views here.

User = get_user_model()


class CommentWrite(APIView):
    permission_classes =[IsAuthenticated]
    def post(self, request):
        user = request.user
        playlist = Playlist.objects.get(id=request.data['playlist_id'])
        comment = Comment.objects.create(writer=user, content=request.data['content'], playlist=playlist, parent=None)
        datas = {
            "message" : "댓글 생성 완료되었습니다.",
        }
        return Response(datas,status=status.HTTP_201_CREATED)
