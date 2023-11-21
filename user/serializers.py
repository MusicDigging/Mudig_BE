from rest_framework import serializers
from .models import Profile, User, Follower
from playlist.models import Playlist

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
        # User의 Playlist 객체를 가져옴
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

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['title', 'thumbnail', 'is_active', 'created_at', 'updated_at', 'music']