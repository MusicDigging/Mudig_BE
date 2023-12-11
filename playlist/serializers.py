from rest_framework import serializers
from .models import Playlist, Music, Like, Comment
from user.serializers import ProfileSerializer

class PlaylistSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Playlist
        fields = '__all__'
        
    def get_like_count(self, obj):
        return obj.like_set.count()
    
    def get_playlist_info(self, obj):
        playlist_info = [{'id': playlist.id, 'thumbnail': playlist.thumbnail,'title':playlist.title} for playlist in obj]
        return playlist_info


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
    
    def get_music_info(self, obj):
        playlist_info = [{'id': music.id, 'thumbnail': music.thumbnail,'singer':music.singer,'song':music.song} for music in obj]
        return playlist_info


class CommentSerializer(serializers.ModelSerializer):
    writer_profile = ProfileSerializer(source='writer.profile', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'writer', 'writer_profile', 'created_at', 'updated_at', 'playlist']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'