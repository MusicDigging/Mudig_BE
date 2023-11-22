from django.urls import path
from .views import Join, SocialJoin, Login, GenerateOtp, Logout, ChangePassWord, Withdrawal, GoogleLogin, GoogleCallback, CheckName, KakaoLogin, KakaoCallback
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
    path("checkname/", CheckName.as_view(), name='check-name'),
    # path("profile/", Profile.as_view(), name='profile'),
    # path("profile/edit/", ProfileUpdate.as_view(), name='pf-edit'),
    # path("follow/", Follow.as_view(), name='follow'),
] 

