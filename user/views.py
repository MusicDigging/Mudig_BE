from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, User, Follower
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404
from playlist.uploads import S3ImgUploader
from rest_framework.parsers import MultiPartParser, FormParser


class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(id=3)  # Test User ID
            profile = get_object_or_404(Profile, user=user)
        except (User.DoesNotExist, Profile.DoesNotExist):
            raise Http404("User or Profile does not exist")

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileEditView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request):
        user = User.objects.get(id=2)  # test
        profile = get_object_or_404(Profile, user=user)
        serializer = ProfileSerializer(profile, data=request.data)

        if 'image' in request.FILES:
            image_file = request.FILES['image']
            uploader = S3ImgUploader(image_file)
            image_url = uploader.upload()
            serializer.initial_data['image'] = image_url

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowAPIView(APIView):
    def post(self, request, user_id):
        target_user = get_object_or_404(User, pk=user_id)
        follower_user = User.objects.get(pk=2)  # test

        if follower_user == target_user:
            return Response({"error": "자기 자신을 팔로우할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        _, created = Follower.objects.get_or_create(target_id=target_user, follower_id=follower_user)
        if created:
            return Response({"status": "팔로우 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "이미 팔로우한 사용자입니다."}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowAPIView(APIView):
    def post(self, request, user_id):
        target_user = get_object_or_404(User, pk=user_id)
        follower_user = User.objects.get(pk=2)  # test
        follow_relation = get_object_or_404(Follower, target_id=target_user, follower_id=follower_user)
        follow_relation.delete()
        return Response({"status": "언팔로우 성공"}, status=status.HTTP_204_NO_CONTENT)

