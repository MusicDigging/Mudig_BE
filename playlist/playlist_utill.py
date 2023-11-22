from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import F
from django.db import models
from .models import Music, Playlist, PlaylistMusic
class PlaylistOrderUpdater:
    def update_order(self, playlist, new_orders):
        ## 모든 values
        playlist_music_list = playlist.playlistmusic_set.all()
        for old_order, new_order in zip(playlist_music_list, new_orders):
            old_order.order = new_order
            old_order.save()

class PlaylistAdder:
    def add_music(self, playlist, music_id):
        music = get_list_or_404(Music, pk__in=music_id)
        playlist.music.add(*music)

class PlaylistRemover:
    def remove_music(self, playlist, music_id):
        music = get_list_or_404(Music, pk__in=music_id)
        print(music)
        playlist.music.remove(*music)
