from django.urls import path
from .views import Join,SocialJoin,Login,GenerateOtp,Logout,ChangePassWord,Withdrawal,GoogleLogin,GoogleCallback,CheckName
from .views import KakaoLogin,KakaoCallback,ProfileView,ProfileEditView,FollowAPIView,UnfollowAPIView,FollowersListView,FollowingListView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'user'

urlpatterns = [
    path('join/', Join.as_view(), name='join'),
    path('socialjoin/', SocialJoin.as_view(), name='social-join'),
    path('login/', Login.as_view(), name='login'),
    path('otp/', GenerateOtp.as_view(), name='otp'),
    path("logout/", Logout.as_view(), name='logout'),
    path("changepassword/", ChangePassWord.as_view(), name='change-pw'),
    path("withdrawal/", Withdrawal.as_view(), name='withdrawal'),
    path("login/google/", GoogleLogin.as_view(), name='google-login'),
    path("login/google/callback/", GoogleCallback.as_view(), name='google-callback'),
    path("checkname/", CheckName.as_view(), name='check-name'),
    path("login/kakao/", KakaoLogin.as_view(), name='kakao-login'),
    path("login/kakao/callback/", KakaoCallback.as_view(), name='kakao-callback'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile-detail'),
    path("profile/edit/", ProfileEditView.as_view(), name='profile-edit'),
    path('<int:user_id>/follow/', FollowAPIView.as_view(), name='follow'),
    path('<int:user_id>/unfollow/', UnfollowAPIView.as_view(), name='unfollow'),
    path('<int:user_id>/followers/', FollowersListView.as_view(), name='user-followers'),
    path('<int:user_id>/following/', FollowingListView.as_view(), name='user-following'),
]