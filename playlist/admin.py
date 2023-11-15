from django.contrib import admin
from .models import Playlist, Music, Comment, Like

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Music)
admin.site.register(Comment)
admin.site.register(Like)