from rest_framework import serializers
from .models import Playlist, Music, Like, Comment

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
    
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
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
        

class InputSerializer(serializers.ModelSerializer):
    situations = serializers.CharField()
    genre = serializers.CharField()
    year = serializers.CharField()

    class Meta:
        model = Playlist
        fields = ['situations','genre','year']
        

class EventSerializer(serializers.ModelSerializer):
    situations = serializers.CharField()

    class Meta:
        model = Playlist
        fields = ['situations']
        

class PlaylistIdSerializer(serializers.ModelSerializer):
    Playlist_id = serializers.CharField()

    class Meta:
        model = Playlist
        fields = ['Playlist_id']

