from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, User, Follower
from .serializers import ProfileSerializer, UserFollowSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404
from playlist.uploads import S3ImgUploader
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated


# 프로필 조회
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 프로필 수정
class ProfileEditView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request):
        # user = User.objects.get(id=2)  # Test User ID
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)

        if 'image' in request.FILES:
            image_file = request.FILES['image']
            uploader = S3ImgUploader(image_file)
            image_url = uploader.upload()
            serializer.initial_data['image'] = image_url

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 팔로우
class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, pk=user_id)
        # follower_user = User.objects.get(pk=3)  # Test User ID

        if request.user == target_user:
            return Response({"error": "자기 자신을 팔로우할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        _, created = Follower.objects.get_or_create(target_id=target_user, follower_id=request.user)
        if created:
            return Response({"status": "팔로우 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "이미 팔로우한 사용자입니다."}, status=status.HTTP_400_BAD_REQUEST)


# 언팔로우
class UnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        target_user = get_object_or_404(User, pk=user_id)
        # follower_user = User.objects.get(pk=3)  # Test User ID
        follow_relation = get_object_or_404(Follower, target_id=target_user, follower_id=request.user)
        follow_relation.delete()
        return Response({"status": "언팔로우 성공"}, status=status.HTTP_204_NO_CONTENT)


# 팔로워 목록 조회
class FollowersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # test_user = get_object_or_404(User, pk=3) # Test User ID
        user = get_object_or_404(User, pk=user_id)
        followers = [follower.follower_id for follower in user.followers.all()]
        serializer = UserFollowSerializer(followers, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# 팔로잉 목록 조회
class FollowingListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, user_id):
        # test_user = get_object_or_404(User, pk=3) # Test User ID
        user = get_object_or_404(User, pk=user_id)
        following = [follow.target_id for follow in user.following.all()]
        serializer = UserFollowSerializer(following, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
