from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiParameter, inline_serializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from json.decoder import JSONDecodeError
from playlist.uploads import S3ImgUploader
from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer
from .serializers import UserSerializer, ChangePasswordSerializer, ProfileSerializer, UserFollowSerializer
from .utils import generate_otp, send_otp_via_email
from .models import Profile, User, Follower
import dotenv
import os
import requests

dotenv.load_dotenv()

CALLBACK_URI = 'http://localhost:3000/login'
GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
GOOGLE_SECRET_KEY = os.environ['GOOGLE_SECRET_KEY']
KAKAO_REST_API_KEY = os.environ['KAKAO_REST_API_KEY']
STATE = os.environ['STATE']


class CheckName(APIView):
    @extend_schema(
        summary="닉네임 유효성 검사 API",
        description="닉네임 유효성 검사 API에 대한 설명 입니다.",
        parameters=[],
        tags=["User"],
        responses=inline_serializer(
            name="Res_Name_Validation",
            fields={
                "name": serializers.CharField(),
            },
        ),
        request=inline_serializer(
            name="Req_Name_Validation",
            fields={
                "name": serializers.CharField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "사용 가능한 닉네임입니다."},
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "이미 사용 중인 닉네임 입니다"},
                },
            ),
        ],
    )
    def post(self, request):
        name = request.data.get('name')
        
        if Profile.objects.filter(name=name).exists():
            return Response({"error":"이미 사용 중인 닉네임 입니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"사용 가능한 닉네임입니다."}, status=status.HTTP_200_OK)


class Join(APIView):
    @extend_schema(
        summary="자체 회원가입 API",
        description="자체 회원가입 API에 대한 설명 입니다.",
        parameters=[],
        tags=["User"],
        responses=inline_serializer(
            name="Res_Join_API",
            fields={
                "email": serializers.CharField(),
                "password": serializers.CharField(),
                "name": serializers.CharField(),
                "about": serializers.CharField(),
                "genre": serializers.CharField(),
                "image": serializers.FileField(),
            },
        ),
        request=inline_serializer(
            name="Req_Join_API",
            fields={
                "email": serializers.CharField(),
                "password": serializers.CharField(),
                "name": serializers.CharField(),
                "about": serializers.CharField(),
                "genre": serializers.CharField(),
                "image": serializers.FileField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "Register success"},
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 404,
                    "res_data": {"error": "프로필 정보를 입력해주세요."},
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 406,
                    "res_data": {"error": "serializer.errors"},
                },
            ),
        ],
    )
    def post(self, request):
        
        user_data = {
            "email": request.data.get('email'),
            "password": request.data.get('password')
        }

        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            user = serializer.save()

            profile = Profile.objects.get(user=user)
            
            name = request.data.get('name')
            about = request.data.get('about')
            genre = request.data.get('genre')
            
            try:
                image = request.FILES['image']
            except:
                is_image = False
            else:
                is_image = True
    
            profile_data = {
                "user": user.id,
                "name": name,
                "about": about,
                "genre": genre,
            }

            if not (name and about and genre):
                user.delete()
                return Response({'error': '프로필 정보를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if is_image:
                img_uploader = S3ImgUploader(image)
                uploaded_url = img_uploader.upload('profile')
                profile_data['image'] = uploaded_url
            
            pf_serializer = ProfileSerializer(profile, profile_data)
            
            if pf_serializer.is_valid():
                pf_serializer.save()
            else:
                return Response(pf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken.for_user(user)
            access_token = str(token.access_token)
            refresh_token = str(token)
            
            message = {
                "message": "회원가입 성공",
                "user" : pf_serializer.data,
                "token" : {               
                    "access": access_token,
                    "refresh": refresh_token,
                }
            }

            return Response(message, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialJoin(APIView):
    @extend_schema(
        summary="소셜 회원가입 API",
        description="소셜 회원가입 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Social Login"],
        responses=inline_serializer(
            name="Res_SocialJoin_API",
            fields={
                "email": serializers.CharField(),
                "name": serializers.CharField(),
                "about": serializers.CharField(),
                "genre": serializers.CharField(),
                "image": serializers.FileField(),
            },
        ),
        request=inline_serializer(
            name="Req_SocialJoin_API",
            fields={
                "email": serializers.CharField(),
                "name": serializers.CharField(),
                "about": serializers.CharField(),
                "genre": serializers.CharField(),
                "image": serializers.FileField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "Register success"},
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "프로필 정보를 입력해주세요."},
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "serializer.errors"},
                },
            ),
        ],
    )
    def post(self, request):
        
        try:
            user = User.objects.create(email=request.data.get('email'), login_method='google')
            user.set_unusable_password()
            user.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            profile = Profile.objects.get(user=user)
            
            name = request.data.get('name')
            about = request.data.get('about')
            genre = request.data.get('genre')
            
            try:
                image = request.FILES['image']
            except:
                is_image = False
            else:
                is_image = True
                
            profile_data = {
                "user": user.id,
                "name": name,
                "about": about,
                "genre": genre,
            }
            
            if not (name and about and genre):
                user.delete()
                return Response({"error" : "프로필 정보를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)

            if is_image:
                img_uploader = S3ImgUploader(image)
                uploaded_url = img_uploader.upload('profile')
                profile_data['image'] = uploaded_url

            pf_serializer = ProfileSerializer(profile, profile_data)

            if pf_serializer.is_valid():
                pf_serializer.save()
            else:
                return Response(pf_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken.for_user(user)
            access_token = str(token.access_token)
            refresh_token = str(token)
            
            message = {
                "message": "회원가입 성공",
                "user" : pf_serializer.data,
                "token" : {               
                    "access": access_token,
                    "refresh": refresh_token,
                }
            }

            return Response(message, status=status.HTTP_200_OK)


class GenerateOtp(APIView):
    @extend_schema(
        summary="이메일 OTP 발급 API",
        description="이메일 OTP 발급 API에 대한 설명 입니다.",
        parameters=[],
        tags=["User"],
        responses=inline_serializer(
            name="Res_GenerateOtp_API",
            fields={
                "email": serializers.CharField(),
            },
        ),
        request=inline_serializer(
            name="Req_GenerateOtp_API",
            fields={
                "email": serializers.CharField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {'message': '인증 번호 생성', 'otp': 'A1B2C3'},
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "이메일 주소를 입력하세요"},
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "이미 가입된 사용자입니다."},
                },
            ),
        ],
    )
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': '이메일 주소를 입력하세요'}, status=status.HTTP_400_BAD_REQUEST)
        
        users = User.objects.filter(email__iexact=email)
        if not users.exists():
            otp = generate_otp()
            send_otp_via_email(email, otp=otp)
            response = {'message': '인증 번호 생성', 'otp': otp}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response({'error': '이미 가입된 사용자입니다.'}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    @extend_schema(
        summary="자체 로그인 API",
        description="자체 로그인 API에 대한 설명 입니다.",
        parameters=[],
        tags=["User"],
        responses=UserSerializer,
        request=inline_serializer(
            name="Login_API",
            fields={
                "email": serializers.CharField(),
                "password": serializers.CharField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "user": {
                            "email": "test@gmail.com",
                            "id": "1"
                        },
                        "message": "Login success",
                        "token": {
                            "access": "eyJhbGci123213iIqwesInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxMjcwMDQwLCJpYXQiOjE3MDEyNjI4NDAsImp0aSI6IjAyNjU5NjkwZmM3YjQ3Njg4YzkxZDUxOThiMDNlMjgyIiwidXNlcl9pZCI6Nn0.TjEFfq-K3Q7Ol31roq7MybH7iJ_r9dW0cbUt9cG9Gac",
                            "refresh": "eyJhbGc123424zI1NasiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMTM0OTI0MCwiaWF0IjoxNzAxMjYyODQwLCJqdGkiOiIxMzk0ZTdhNWJiM2Y0MzQ0Yjk0OWU3MWYyNDhjMzQ4YyIsInVzZXJfaWQiOjZ9.1eTJK2LgWV8KprCO-HcvaZyg6GjVsnQl7PlkvzuJPhM"
                        }
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="401_UNAUTHORIZED",
                value={
                    "status": 401,
                    "res_data": {"error": "이메일 또는 비밀번호가 일치하지 않습니다."},
                },
            ),
        ],
    )
    def post(self, request):
        user = authenticate(
            email = request.data.get('email'),
            password = request.data.get('password')
        )
        
        if user is not None:
            serializer = ProfileSerializer(user.profile)
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
            return Response({"error": "이메일 또는 비밀번호가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="로그아웃 API",
        description="로그아웃 API에 대한 설명 입니다.",
        parameters=[],
        tags=["User"],
        responses=UserSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "message": "로그아웃 성공",
                    },
                }
            ),
        ],
    )
    def post(self, request):
        user = request.user
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()
        logout(request)
        return Response({"message":"로그아웃 성공"},status=status.HTTP_200_OK)


class ChangePassWord(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="비밀번호 변경 API",
        description="비밀번호 변경 API에 대한 설명 입니다.",
        parameters=[],
        tags=["User"],
        responses=ChangePasswordSerializer,
        request=inline_serializer(
            name="Change_Password",
            fields={
                "old_password": serializers.CharField(),
                "new_password": serializers.CharField()
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {"message": "비밀번호가 성공적으로 변경되었습니다."},
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "현재 비밀번호가 일치하지 않습니다."},
                },
            ),
        ],
    )
    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response({"error": "현재 비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
                
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            
            return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)


# 프로필 조회
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="프로필 조회 API",
        description="프로필 조회 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Profile"],
        responses=inline_serializer(
            name="Get_Profile",
            fields={
                "profile": serializers.CharField(),
                "playlist": serializers.CharField()
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "profile": "profile",
                        "playlist": "Playlist"
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {"error": "프로필 정보를 찾을 수 없습니다."},
                },
            ),
        ],
    )
    def get(self, request, user_id):
        user = get_object_or_404(User,pk=user_id)
        profile = get_object_or_404(Profile, user=user)
        pf_serializer = ProfileSerializer(profile)
        playlists = Playlist.objects.filter(writer=user)
        py_serializer = PlaylistSerializer(playlists, many=True)
        data = {
            "profile": pf_serializer.data,
            "playlist": py_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)


# 프로필 수정
class ProfileEditView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    @extend_schema(
        summary="프로필 수정 API",
        description="프로필 수정 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Profile"],
        responses=ProfileSerializer,
        request=ProfileSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "message": "프로필 수정이 완료되었습니다."
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {"error": "프로필 정보를 찾을 수 없습니다."},
                },
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {"error": "올바르지 않은 프로필 데이터입니다."},
                },
            ),
        ],
    )
    def put(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)

        if 'image' in request.FILES:
            image_file = request.FILES['image']
            uploader = S3ImgUploader(image_file)
            image_url = uploader.upload('profile')
            serializer.initial_data['image'] = image_url

        rep_playlist_id = request.data.get('rep_playlist')
        if rep_playlist_id:
            try:
                rep_playlist = Playlist.objects.get(pk=rep_playlist_id)
                serializer.initial_data['rep_playlist'] = rep_playlist.id
            except Playlist.DoesNotExist:
                return Response({"error": "대표 플레이리스트가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "프로필 수정이 완료되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Withdrawal(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="회원 탈퇴 API",
        description="회원 탈퇴 API에 대한 설명 입니다.",
        parameters=[],
        responses=UserSerializer,
        tags=["User"],
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "message": "회원탈퇴 되었습니다."
                    },
                }
            ),
        ],
    )
    def delete(self, request):
        user = request.user
        provided_password = request.data.get('password', None)
        if not provided_password or not check_password(provided_password, user.password):
            return Response({"error": "비밀번호가 정확하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()
        
        user.is_active = False
        user.save()
        
        return Response({"message": "회원탈퇴 되었습니다."}, status=status.HTTP_200_OK)


class GoogleLogin(APIView):
    @extend_schema(
        summary="구글 로그인 API",
        description="구글 로그인 API에 대한 설명 입니다.",
        parameters=[],
        responses=UserSerializer,
        tags=["Social Login"],
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "data": f"https://accounts.google.com/o/oauth2/v2/auth?client_id=GOOGLE_CLIENT_ID&response_type=code&redirect_uri=CALLBACK_URI&scope=https://www.googleapis.com/auth/userinfo.email"
                    },
                }
            ),
        ],
    )
    def get(self, request):
        data = {
            'url': f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&response_type=code&redirect_uri={CALLBACK_URI}&scope=https://www.googleapis.com/auth/userinfo.email"
        }
        return Response(data,status=status.HTTP_200_OK)


class GoogleCallback(APIView):
    @extend_schema(
        summary="구글 로그인 콜백 API",
        description="구글 로그인 콜백 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Social Login"],
        responses=ProfileSerializer,
        request=inline_serializer(
            name="GoogleCallback",
            fields={
                "code": serializers.CharField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="가입이력있음",
                value={
                    "status": 200,
                    "res_data": {
                        "user": {
                            "email": "test@gmail.com",
                            "id": "1"
                        },
                        "message": "Login success",
                        "token": {
                            "access": "eyJhbGci123213iIqwesInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxMjcwMDQwLCJpYXQiOjE3MDEyNjI4NDAsImp0aSI6IjAyNjU5NjkwZmM3YjQ3Njg4YzkxZDUxOThiMDNlMjgyIiwidXNlcl9pZCI6Nn0.TjEFfq-K3Q7Ol31roq7MybH7iJ_r9dW0cbUt9cG9Gac",
                            "refresh": "eyJhbGc123424zI1NasiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMTM0OTI0MCwiaWF0IjoxNzAxMjYyODQwLCJqdGkiOiIxMzk0ZTdhNWJiM2Y0MzQ0Yjk0OWU3MWYyNDhjMzQ4YyIsInVzZXJfaWQiOjZ9.1eTJK2LgWV8KprCO-HcvaZyg6GjVsnQl7PlkvzuJPhM"
                        }
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="가입이력없음",
                value={
                    "status": 200,
                    "res_data": {
                        "email": "test@gmail.com",
                        "message": "프로필 생성 진행"
                        
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": f"failed to get email"
                    },
                }
            ),
        ],
    )
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
            return Response({'error': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

        email_req_json = email_req.json()
        email = email_req_json.get('email')

        try: # 이미 가입된 유저인지 확인
            user = User.objects.get(email=email)
            refresh = RefreshToken.for_user(user)
            token={
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
            serializer = ProfileSerializer(user.profile)
            response = {
                "message": "로그인 성공",
                "token": token,
                "user": serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            response = {
                "message": "프로필 생성 진행",
                "email": email,
            }
            return Response(data=response, status=status.HTTP_200_OK)


class KakaoLogin(APIView):
    @extend_schema(
        summary="카카오 로그인 API",
        description="카카오 로그인 API에 대한 설명 입니다.",
        parameters=[],
        responses=UserSerializer,
        tags=["Social Login"],
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "data": f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=KAKAO_REST_API_KEY&redirect_uri=CALLBACK_URI"
                    },
                }
            ),
        ],
    )
    def get(self, request):
        data = {
            'url': f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={KAKAO_REST_API_KEY}&redirect_uri={CALLBACK_URI}"
        }
        return Response(data,status=status.HTTP_200_OK)


class KakaoCallback(APIView):
    @extend_schema(
        summary="카카오 로그인 콜백 API",
        description="카카오 로그인 콜백 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Social Login"],
        responses=ProfileSerializer,
        request=inline_serializer(
            name="KakaoCallback",
            fields={
                "code": serializers.CharField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="가입이력있음",
                value={
                    "status": 200,
                    "res_data": {
                        "user": {
                            "email": "test@gmail.com",
                            "id": "1"
                        },
                        "message": "Login success",
                        "token": {
                            "access": "eyJhbGci123213iIqwesInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxMjcwMDQwLCJpYXQiOjE3MDEyNjI4NDAsImp0aSI6IjAyNjU5NjkwZmM3YjQ3Njg4YzkxZDUxOThiMDNlMjgyIiwidXNlcl9pZCI6Nn0.TjEFfq-K3Q7Ol31roq7MybH7iJ_r9dW0cbUt9cG9Gac",
                            "refresh": "eyJhbGc123424zI1NasiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMTM0OTI0MCwiaWF0IjoxNzAxMjYyODQwLCJqdGkiOiIxMzk0ZTdhNWJiM2Y0MzQ0Yjk0OWU3MWYyNDhjMzQ4YyIsInVzZXJfaWQiOjZ9.1eTJK2LgWV8KprCO-HcvaZyg6GjVsnQl7PlkvzuJPhM"
                        }
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="가입이력없음",
                value={
                    "status": 200,
                    "res_data": {
                        "email": "test@gmail.com",
                        "message": "프로필 생성 진행"
                        
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": f"failed to get email"
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": f"This AccessToken Doses Not Exist"
                    },
                }
            ),
        ],
    )
    def post(self, request):
        code = request.data['code']

        # body에 해당 값을 포함시켜서 보내는 부분입니다.
        request_data = {
            'grant_type': 'authorization_code',
            'client_id': KAKAO_REST_API_KEY,
            'redirect_uri': "http://localhost:3000/login",
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
            return Response({'error': 'This AccessToken Doses Not Exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        # kakao 회원정보 요청하는 부분입니다. 헤더에 추가해주는 부분이 구글과는 달라서 주석 달아드려요
        auth_headers = {
            "Authorization": f'Bearer ${access_token}',
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }

        user_info_res = requests.post("https://kapi.kakao.com/v2/user/me", headers=auth_headers)
        user_info_json = user_info_res.json()

        kakao_account = user_info_json.get('kakao_account')

        if not kakao_account:
            return Response({'error': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = kakao_account.get('email')

        try:
            user = User.objects.get(email=email)
            refresh = RefreshToken.for_user(user)
            token={
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
            serializer = ProfileSerializer(user.profile) # 변동 가능성 있음
            response = {
                "message": "로그인 성공",
                "token": token,
                "user": serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            response = {
                "message": "프로필 생성 진행",
                "email": email,
            }
            return Response(data=response, status=status.HTTP_200_OK)

# 팔로우
class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="팔로우 기능 API",
        description="팔로우 기능 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Follow"],
        responses=UserFollowSerializer,
        request=inline_serializer(
            name="FollowAPIView",
            fields={
                "user_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="201_CREATED",
                value={
                    "status": 201,
                    "res_data": {
                        "message": "팔로우 성공"
                        
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": f"이미 팔로우한 사용자입니다."
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="400_BAD_REQUEST",
                value={
                    "status": 400,
                    "res_data": {
                        "error": f"자기 자신을 팔로우할 수 없습니다."
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": f"해당 유저를 찾을 수 없습니다."
                    },
                }
            ),
        ],
    )
    def post(self, request):
        user_id = request.data['user_id']
        target_user = get_object_or_404(User, pk=user_id)

        if request.user == target_user:
            return Response({"error": "자기 자신을 팔로우할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        _, created = Follower.objects.get_or_create(target_id=target_user, follower_id=request.user)
        if created:
            return Response({"message": "팔로우 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "이미 팔로우한 사용자입니다."}, status=status.HTTP_400_BAD_REQUEST)


# 언팔로우
class UnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="언팔로우 기능 API",
        description="언팔로우 기능 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Follow"],
        responses=UserFollowSerializer,
        request=inline_serializer(
            name="FollowAPIView",
            fields={
                "user_id": serializers.IntegerField(),
            },
        ),
        examples=[
            OpenApiExample(
                response_only=True,
                name="201_CREATED",
                value={
                    "status": 201,
                    "res_data": {
                        "message": "언팔로우 성공"
                        
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": f"해당 유저를 찾을 수 없습니다."
                    },
                }
            ),
        ],
    )
    def delete(self, request):
        user_id = request.data['user_id']
        target_user = get_object_or_404(User, pk=user_id)
        # follower_user = User.objects.get(pk=3)  # Test User ID
        follow_relation = get_object_or_404(Follower, target_id=target_user, follower_id=request.user)
        follow_relation.delete()
        return Response({"message": "언팔로우 성공"}, status=status.HTTP_204_NO_CONTENT)


# 팔로워 목록 조회
class FollowersListView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="팔로워 목록 조회 기능 API",
        description="팔로워 목록 조회 기능 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Follow"],
        responses=UserFollowSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "follow_list": "serializer.data"
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": f"해당 유저를 찾을 수 없습니다."
                    },
                }
            ),
        ],
    )
    def get(self, request, user_id):
        # test_user = get_object_or_404(User, pk=3) # Test User ID
        user = get_object_or_404(User, pk=user_id)
        followers = [follower.follower_id for follower in user.followers.all()]
        serializer = UserFollowSerializer(followers, many=True, context={'request': request})
        return Response({"follower_list": serializer.data}, status=status.HTTP_200_OK)


# 팔로잉 목록 조회
class FollowingListView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="팔로잉 목록 조회 기능 API",
        description="팔로잉 목록 조회 기능 API에 대한 설명 입니다.",
        parameters=[],
        tags=["Follow"],
        responses=UserFollowSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                name="200_OK",
                value={
                    "status": 200,
                    "res_data": {
                        "following_list": "serializer.data"
                    },
                }
            ),
            OpenApiExample(
                response_only=True,
                name="404_NOT_FOUND",
                value={
                    "status": 404,
                    "res_data": {
                        "error": f"해당 유저를 찾을 수 없습니다."
                    },
                }
            ),
        ],
    )
    def get(self, request, user_id):
        # test_user = get_object_or_404(User, pk=3) # Test User ID
        user = get_object_or_404(User, pk=user_id)
        following = [follow.target_id for follow in user.following.all()]
        serializer = UserFollowSerializer(following, many=True, context={'request': request})
        return Response({"following_list": serializer.data}, status=status.HTTP_200_OK)
