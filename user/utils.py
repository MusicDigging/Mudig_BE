import random
from django.core.mail import send_mail
from django.conf import settings
from .models import User

def generate_otp():
    otp = str(random.randint(100000, 999999))
    return otp


def send_otp_via_email(email, otp):
    subject = '[MusicDigging] 환영합니다! 이메일을 인증해 주세요.'
    message = f'아래의 코드를 입력하면 회원가입이 완료됩니다. \nCODE: {otp}'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])