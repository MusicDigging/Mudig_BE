from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.views import APIView
from .models import Profile, User
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404


class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(id=2)
            profile = Profile.objects.get(user=user)
        except (User.DoesNotExist, Profile.DoesNotExist):
            raise Http404("User or Profile does not exist")
        
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileEditView(APIView):
    # permission_classes = [IsAuthenticated]
    def put(self, request):
        user = get_object_or_404(User, id=2) #test
        profile = get_object_or_404(Profile, user=user)

        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


