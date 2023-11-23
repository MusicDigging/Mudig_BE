from django.urls import path
from .views import ProfileView, ProfileEditView, FollowAPIView, UnfollowAPIView, FollowersListView, FollowingListView
# from .views import Join, Login, Logout, ProfileUpdate, ChangePassWord
# 해당 부분은 수정해주시면 됩니다.

app_name = 'user'

urlpatterns = [
    # path("register/", Join.as_view(), name='join'),
    # path("login/", Login.as_view(), name="login"),
    # path("logout/", Logout.as_view(), name='logout'),
    # path("changePassword/", ChangePassWord.as_view(), name='change-pw'),
    # path("withdrawal/", Withdrawal.as_view(), name='withdrawal'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("profile/edit/", ProfileEditView.as_view(), name='profile-edit'),
    path('users/<int:user_id>/follow/', FollowAPIView.as_view(), name='follow'),
    path('users/<int:user_id>/unfollow/', UnfollowAPIView.as_view(), name='unfollow'),
    path('users/<int:user_id>/followers/', FollowersListView.as_view(), name='user-followers'),
    path('users/<int:user_id>/following/', FollowingListView.as_view(), name='user-following'),
] 

