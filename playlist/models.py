from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Music(models.Model):
    information = models.CharField(max_length=200) # 임시로 넣어놨습니다. 추가 수정이 들어갈 필드입니다.
    singer = models.CharField(max_length=200)
    song = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    thumbnail = models.URLField(null = True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    music = models.ManyToManyField(Music)


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
