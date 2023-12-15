from django.shortcuts import get_object_or_404, get_list_or_404
from django.db import models
from .models import Music, Playlist, PlaylistMusic


class PlaylistOrderUpdater:
    def update_order(self, playlist, new_orders):
        ## 모든 values
        for ordering, music in enumerate(new_orders, start = 1):
            music_order = PlaylistMusic.objects.get(playlist = playlist, music_id=music)
            music_order.order = ordering
            music_order.save()
            


class PlaylistAdder:
    def add_music(self, playlist, music_id):
        music = get_list_or_404(Music, pk__in=music_id)
        # playlist.music.add(*music)
        max_order = (
            PlaylistMusic.objects.filter(playlist=playlist)
            .aggregate(models.Max('order'))['order__max'] or 0
        )
        
        # 테스트1
        for order, music_id in enumerate(music_id, start=max_order):
            music = Music.objects.get(id=music_id)
            exist_music = PlaylistMusic.objects.filter(playlist=playlist, music_id=music)
            if exist_music:
                data = {
                    "message" :"이미 플리안에 들어있는 노래입니다."
                }
                return data
            else:
                PlaylistMusic.objects.create(playlist=playlist, music=music, order= order + 1)


class PlaylistRemover:
    def remove_music(self, playlist, music_list):
        music_instances = get_list_or_404(Music, pk__in=music_list)
        playlist_all_music = list(playlist.playlistmusic_set.all())
        # PlaylistMusic에서 해당하는 레코드 삭제
        
        deleted_records = playlist.playlistmusic_set.filter(music__in=music_instances)
        filtered_list = [item for item in playlist_all_music if item not in deleted_records]
        
        deleted_records.delete()
        for new_order, music in enumerate(filtered_list, start = 1):
            music.order = new_order
            music.save()
