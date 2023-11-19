from django.contrib.auth import authenticate
from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .utils import generate_otp, send_otp_via_email

class Join(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            res = Response(
                {
                    "user" : serializer.data,
                    "message" : "Register success",
                },
                status = status.HTTP_200_OK,
            )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GenerateOtp(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({'message': '이메일 주소를 입력하세요.'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             user = User.objects.get(email=email)
#         except:
#             otp = generate_otp()
#             send_otp_via_email(email, otp=otp)
        
#             response = {'message': '인증 번호 생성', 'otp': otp}
#             return Response(data=response, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': '이미 가입된 사용자입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
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
            email=request.data.get('email'),
            password=request.data.get('password')
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
            return Response(status=status.HTTP_400_BAD_REQUEST)