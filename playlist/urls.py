from django.urls import path
from .views import List, Delete, Detail, Create, Update, Add, MyPlaylist, Allmusiclist, RandomMovieView, EventPlaylistGenerate

app_name = 'playlist'

urlpatterns = [
    # home
    # path('', PlaylistView.as_view() , name='list'),
    path('', List.as_view() , name='list'),
    # playlist CRUD
    path('detail/<int:pk>/', Detail.as_view() , name='detail'),
    path('create/', Create.as_view() , name='write'),
    path('delete/', Delete.as_view() , name='delete'),
    path('detail/<int:pk>/edit/', Update.as_view() , name='edit'),
    path('add/', Add.as_view() , name='add'),
    path('myplaylist/', MyPlaylist.as_view() , name='myplaylist'),
    path('music/', Allmusiclist.as_view() , name='music'),
    # path('search/', Search.as_view() , name='search'),
    # path('like/', Like.as_view() , name='like'),
    # comment
    # path('comment/write/', CommentWrite.as_view() , name='cm-write'),
    # path('comment/edit/', CommentEdit.as_view() , name='cm-edit'),
    # path('comment/delete/', CommentDelete.as_view() , name='cm-delete'),
    path('random-mv/', RandomMovieView.as_view() , name='random-mv'),
    path('event/', EventPlaylistGenerate.as_view() , name='event'),
]
