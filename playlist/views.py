from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Playlist, Comment, Like as Like_Model
from .serializers import CommentSerializer
from rest_framework.views import APIView
# Create your views here.

User = get_user_model()

class Like(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        try:
            playlist = Playlist.objects.get(id=request.data['playlist_id'])
            like, created = Like_Model.objects.get_or_create(playlist=playlist, user=user)
        except ObjectDoesNotExist:
            raise Http404

        if created:
            return Response({"detail":"좋아요 성공했습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail":"이미 좋아요를 눌렀습니다."}, status=status.HTTP_400_BAD_REQUEST)


class CommentWrite(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        playlist = Playlist.objects.get(id=request.data['playlist_id'])
        comment = Comment.objects.create(writer=user, content=request.data['content'], playlist=playlist, parent=None)
        datas = {
            "message" : "댓글 생성 완료되었습니다.",
        }
        return Response(datas,status=status.HTTP_201_CREATED)
    

class CommentDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        try:
            playlist = Playlist.objects.get(id=request.data['playlist_id'])
            comment = Comment.objects.get(id=request.data['comment_id'], writer = user)
        except ObjectDoesNotExist:
            raise Http404
        # comment = Comment.objects.get(id=request.data['comment_id'])
        playlist.is_active = False
        comment.is_active = False
        comment.delete()

        datas = {
            "message" : "댓글 삭제 완료되었습니다."
        }
        return Response(datas, status=status.HTTP_200_OK)


# class CommentDelete(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self, request):
#         user = request.user
#         try:
#             playlist = Playlist.objects.get(id=request.data['playlist_id'])
#             comment = Comment.objects.get(id=request.data['comment_id'])
#         except ObjectDoesNotExist:
#             raise Http404

#         if comment.writer != user:
#             # 작성자와 현재 사용자가 다른 경우 권한 거부 예외를 발생시킴
#             raise PermissionDenied("작성자만 댓글을 삭제할 수 있습니다.")

#         playlist.is_active = False
#         comment.is_active = False
#         comment.delete()

#         datas = {
#             "message": "댓글 삭제 완료되었습니다."
#         }
#         return Response(datas, status=status.HTTP_200_OK)


class CommentEdit(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        # playlist = Playlist.comment.get(id=request.data['playlist_id'])
        try:
            playlist = Playlist.objects.get(id=request.data['playlist_id'])
            comment = Comment.objects.get(id=request.data['comment_id'], writer = user)
        except ObjectDoesNotExist:
            raise Http404
        
        comment.content = request.data.get('content', comment.content)
        comment.save()
        data = {
            "message" : "댓글 수정 완료되었습니다."
        }
        return Response(data, status=status.HTTP_200_OK)
