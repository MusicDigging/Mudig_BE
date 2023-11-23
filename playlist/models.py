from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

User = get_user_model()

class Music(models.Model):
    information = models.CharField(max_length=200) # 임시로 넣어놨습니다. 추가 수정이 들어갈 필드입니다.
    singer = models.CharField(max_length=200)
    song = models.CharField(max_length=200)
    thumbnail = models.URLField(null = True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    music = models.ManyToManyField(Music, through='PlaylistMusic', related_name='playlists')
    # music = models.ManyToManyField(Music, through='PlaylistMusicOrder')


class PlaylistMusic(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']


class Comment(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# @receiver(post_save, sender=PlaylistMusic)
# def update_order_on_save(sender, instance, **kwargs):
#     """
#     플레이리스트 뮤직이 저장될 때 호출되는 시그널 핸들러.
#     저장 후 해당 플레이리스트 내의 뮤직들의 순서를 업데이트합니다.
#     """
#     update_order(instance.playlist)

# @receiver(post_delete, sender=PlaylistMusic)
# def update_order_on_delete(sender, instance, **kwargs):
#     """
#     플레이리스트 뮤직이 삭제될 때 호출되는 시그널 핸들러.
#     삭제 후 해당 플레이리스트 내의 뮤직들의 순서를 업데이트합니다.
#     """
#     update_order(instance.playlist)

# def update_order(playlist):
#     """
#     플레이리스트 내의 뮤직들의 순서를 업데이트합니다.
#     """
#     playlist_music_list = PlaylistMusic.objects.filter(playlist=playlist).order_by('order')
#     for i, playlist_music in enumerate(playlist_music_list, start=1):
#         playlist_music.order = i
#         playlist_music.save()