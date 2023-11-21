from django.urls import path
from .views import List, Delete, Detail, Create, Update, Add

app_name = 'playlist'

urlpatterns = [
    # home
    path('', List.as_view() , name='list'),
    # playlist CRUD
    path('detail/<int:pk>/', Detail.as_view() , name='detail'),
    path('create/', Create.as_view() , name='write'),
    path('delete/', Delete.as_view() , name='delete'),
    path('detail/<int:pk>/edit/', Update.as_view() , name='edit'),
    path('add/', Add.as_view() , name='add'),
    # path('search/', Search.as_view() , name='search'),
    # path('like/', Like.as_view() , name='like'),
    # comment
    # path('comment/write/', CommentWrite.as_view() , name='cm-write'),
    # path('comment/edit/', CommentEdit.as_view() , name='cm-edit'),
    # path('comment/delete/', CommentDelete.as_view() , name='cm-delete'),
    # path('random-mv/', RandomMovie.as_view() , name='random-mv')
]
