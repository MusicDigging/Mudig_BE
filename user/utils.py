import random
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import User

def generate_otp():
    otp = str(random.randint(100000, 999999))
    return otp


def send_otp_via_email(email, otp):
    subject = '[MusicDigging] 환영합니다! 이메일을 인증해 주세요.'
    context = {'otp': otp, 'email': settings.EMAIL_HOST_USER}
    message = render_to_string('user/email_template.html', context)
    send_mail(subject, '', settings.EMAIL_HOST_USER, [email], html_message=message)