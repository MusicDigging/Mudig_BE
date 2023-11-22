from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout
from django.shortcuts import render
from .serializers import UserSerializer, ChangePasswordSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Profile
from .utils import generate_otp, send_otp_via_email
from playlist.uploads import S3ImgUploader
import dotenv
import os
import requests

dotenv.load_dotenv()


class CheckName(APIView):
    def post(self, request):
        name = request.data.get('name')
        
        if Profile.objects.filter(name=name).exists():
            return Response({"error":"이미 사용 중인 닉네임 입니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"사용 가능한 닉네임입니다."}, status=status.HTTP_200_OK)


class Join(APIView):
    def post(self, request):
        
        user_data = {
            "email": request.data.get('email'),
            "password": request.data.get('password')
        }

        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            user = serializer.save()

            profile = Profile.objects.get(user=user)
            
            try:
                image = request.FILES['image']
            except:
                is_image = False
            else:
                is_image = True
    
                profile_data = {
                    "user": user.id,
                    "name": request.data.get('name'),
                    "about": request.data.get('about'),
                    "genre": request.data.get('genre')
                }
            
            if is_image:
                img_uploader = S3ImgUploader(image)
                uploaded_url = img_uploader.upload('profile')
                profile_data['image'] = uploaded_url
            
            pf_serializer = ProfileSerializer(profile, profile_data)

            if pf_serializer.is_valid():
                pf_serializer.save()
            else:
                return Response(pf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            message = {
                "message" : "Register success"
            }

            return Response(message, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialJoin(APIView):
    def post(self, request):
        
        try:
            user = User.objects.create(email=request.data.get('email'), login_method='google')
            user.set_unusable_password()
            user.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            profile = Profile.objects.get(user=user)
            
            try:
                image = request.FILES['image']
            except:
                is_image = False
            else:
                is_image = True
                
            profile_data = {
                "user": user.id,
                "name": request.data.get('name'),
                "about": request.data.get('about'),
                "genre": request.data.get('genre')
            }

            if is_image:
                img_uploader = S3ImgUploader(image)
                uploaded_url = img_uploader.upload('profile')
                profile_data['image'] = uploaded_url

            pf_serializer = ProfileSerializer(profile, profile_data)

            if pf_serializer.is_valid():
                pf_serializer.save()
            else:
                return Response(pf_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

            message = {
                "message" : "Register success",
                "profile" : pf_serializer.data,
            }

            return Response(message, status=status.HTTP_200_OK)


class GenerateOtp(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'message': '이메일 주소를 입력하세요'}, status=status.HTTP_400_BAD_REQUEST)
        
        users = User.objects.filter(email__iexact=email)
        if not users.exists():
            otp = generate_otp()
            send_otp_via_email(email, otp=otp)
            response = {'message': '인증 번호 생성', 'otp': otp}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response({'message': '이미 가입된 사용자입니다.'}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):    
        user = authenticate(
            email = request.data.get('email'),
            password = request.data.get('password')
        )
        if user is not None:
            serializer = UserSerializer(user)
            
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user" : serializer.data,
                    "message" : "Login success",
                    "token" : {
                        "access" : access_token,
                        "refresh" : refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response({"message": "인증 실패"}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()
        logout(request)
        return Response({"message":"로그아웃 성공"},status=status.HTTP_200_OK)


class ChangePassWord(APIView):
    permission_classes = [IsAuthenticated]
        
    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response({"messsage": "현재 비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
                
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            
            return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Withdrawal(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        user = request.user
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()
        
        user.is_active = False
        user.save()
        
        return Response({"message": "회원탈퇴 되었습니다."}, status=status.HTTP_200_OK)


CALLBACK_URI = 'http://127.0.0.1:5500/index.html'
GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
GOOGLE_SECRET_KEY = os.environ['GOOGLE_SECRET_KEY']
KAKAO_REST_API_KEY = 'kakao_restapi_key'
STATE = os.environ['STATE']


class GoogleLogin(APIView):
    def post(self, request):
        data = {
            'url': f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&response_type=code&redirect_uri={CALLBACK_URI}&scope=https://www.googleapis.com/auth/userinfo.email"
        }
        return Response(data)


class GoogleCallback(APIView):
    def post(self, request):
        code = request.data['code']

        token_req = requests.post(f"https://oauth2.googleapis.com/token?client_id={GOOGLE_CLIENT_ID}&client_secret={GOOGLE_SECRET_KEY}&code={code}&grant_type=authorization_code&redirect_uri={CALLBACK_URI}&state={STATE}")

        token_req_json = token_req.json()
        error = token_req_json.get("error")

        if error is not None:
            raise JSONDecodeError(error)

        access_token = token_req_json.get('access_token')

        email_req = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
        email_req_status = email_req.status_code

        if email_req_status != 200:
            return Response({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

        email_req_json = email_req.json()
        email = email_req_json.get('email')

        try: # 이미 가입된 유저인지 확인
            user = User.objects.get(email=email)
            refresh = RefreshToken.for_user(user)
            token={
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
            serializer = UserSerializer(user) # 변동 가능성 있음
            response = {
                "message": "로그인 성공",
                "token": token,
                "user_info": serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            response = {
                "message": "프로필 생성 진행",
                "email": email,
            }
            return Response(data=response, status=status.HTTP_200_OK)


class KakaoLogin(APIView):
    def post(self, request):
        data = {
            'url': f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=${KAKAO_REST_API_KEY}&redirect_uri=${CALLBACK_URI}"
        }
        return Response(data)


class KakaoCallback(APIView):
    def post(self, request):
        code = request.data['code']

        # body에 해당 값을 포함시켜서 보내는 부분입니다.
        request_data = {
            'grant_type': 'authorization_code',
            'client_id': KAKAO_REST_API_KEY,
            'redirect_uri': CALLBACK_URI,
            'code': code,
        }
        # header에 content-type을 지정해주는 부분입니다.
        token_headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        token_res = requests.post("https://kauth.kakao.com/oauth/token", data=request_data, headers=token_headers)
        
        token_json = token_res.json()
        access_token = token_json.get('access_token')
        
        if not access_token:
            return Response({'err_msg': 'This AccessToken Doses Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

        # kakao 회원정보 요청하는 부분입니다. 헤더에 추가해주는 부분이 구글과는 달라서 주석 달아드려요
        auth_headers = {
            "Authorization": access_token,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        user_info_res = requests.get("https://kapi.kakao.com/v2/user/me", headers=auth_headers)
        user_info_json = user_info_res.json()

        kakao_account = user_info_json.get('kakao_account')
        if not kakao_account:
            return Response({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = kakao_account.get('email')
        
        try:
            user = User.objects.get(email=email)
            token = create_jwt_pair_for_user(user)
            serializer = UserSerializer(user)
            follower = Follower.objects.filter(follower_id=user).values()
            notify = Notification.objects.filter(receiver=user,is_read=False).values()
            response = {
                "message": "로그인 성공",
                "token": token,
                "user_info": serializer.data,
                "follower": follower,
                "notify": notify,
            }
            return Response(data=response, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            response = {
                "message": "프로필 생성 진행",
                "email": email,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)