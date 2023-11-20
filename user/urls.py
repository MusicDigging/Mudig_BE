from django.urls import path
from .views import Join, Login, GenerateOtp, Logout, ChangePassWord
from rest_framework_simplejwt.views import TokenRefreshView
# from .views import Join, Login, Logout, ProfileUpdate, ChangePassWord
# 해당 부분은 수정해주시면 됩니다.

app_name = 'user'

urlpatterns = [
    path('join/', Join.as_view(), name='join'),
    path('login/', Login.as_view(), name='login'),
    path('otp/', GenerateOtp.as_view(), name='otp'),
    path("logout/", Logout.as_view(), name='logout'),
    path("changepassword/", ChangePassWord.as_view(), name='change-pw'),
    # path("withdrawal/", Withdrawal.as_view(), name='withdrawal'),
    # path("profile/", Profile.as_view(), name='profile'),
    # path("profile/edit/", ProfileUpdate.as_view(), name='pf-edit'),
    # path("follow/", Follow.as_view(), name='follow'),
] 

