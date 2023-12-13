from rest_framework import serializers
from .models import User, Profile, Follower
from playlist.models import Playlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
            )
        
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True)
    is_following = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['id', 'name', 'image', 'about', 'genre', 'email', 'rep_playlist', 'is_following' ]
    def get_is_following(self, obj):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            if obj.user == request.user:
                return None
            return Follower.objects.filter(target_id=obj.user, follower_id=request.user).exists()
        return False


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserFollowSerializer(serializers.ModelSerializer):
    profile_image = serializers.CharField(source='profile.image')
    nickname = serializers.CharField(source='profile.name')
    is_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'profile_image', 'nickname', 'is_following']

    def get_is_following(self, obj):
        # 팔로잉 목록 
        # test_user_id = 2  # Test User id
        request_user = self.context['request'].user
        return Follower.objects.filter(follower_id=request_user, target_id=obj).exists()


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['title', 'thumbnail', 'is_active', 'created_at', 'updated_at', 'music']