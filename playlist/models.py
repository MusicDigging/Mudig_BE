from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

User = get_user_model()

class Music(models.Model):
    information = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    song = models.CharField(max_length=200)
    thumbnail = models.URLField(null = True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    music = models.ManyToManyField(Music, through='PlaylistMusic', related_name='playlists')
    is_public = models.BooleanField(default=True)


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
