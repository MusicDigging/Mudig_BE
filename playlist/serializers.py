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

