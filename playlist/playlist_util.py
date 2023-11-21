from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Music, Playlist
class PlaylistOrderUpdater:
    def update_order(self, playlist, new_order):
        # 플레이리스트 안의 곡 순서를 수정하는 구현
        pass

class PlaylistAdder:
    def add_music(self, playlist, music_id):
        music = get_list_or_404(Music, pk__in=music_id)
        playlist.music.add(*music)

class PlaylistRemover:
    def remove_music(self, playlist, music_id):
        music = get_list_or_404(Music, pk__in=music_id)
        print(music)
        playlist.music.remove(*music)