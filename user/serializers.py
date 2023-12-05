from rest_framework import serializers
from .models import User, Profile, Follower
from playlist.models import Playlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
            )
        
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    

class ProfileSerializer(serializers.ModelSerializer):
    playlists = serializers.SerializerMethodField()
    representative_playlist = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['name', 'image', 'about', 'genre', 'playlists', 'representative_playlist', 'followers_count', 'following_count']

    def get_genres(self, obj):
        # 선택한 장르
        return [genre.name for genre in obj.genres.all()]

    def get_playlists(self, obj):
        # User의 Playlist 
        playlists = Playlist.objects.filter(writer=obj.user)
        return PlaylistSerializer(playlists, many=True).data

    def get_representative_playlist(self, obj):
        # 대표 플레이리스트
        playlist = Playlist.objects.filter(writer=obj.user).order_by('-created_at').first()
        return PlaylistSerializer(playlist).data if playlist else None

    def get_followers_count(self, obj):
        # 팔로워 수
        return Follower.objects.filter(target_id=obj.user).count()

    def get_following_count(self, obj):
        # 팔로잉 수
        return Follower.objects.filter(follower_id=obj.user).count()


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
