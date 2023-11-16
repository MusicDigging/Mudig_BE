from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    # create_user
    def create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('이미 있는 Email 입니다.')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            created_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_superuser
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password,is_superuser=True, is_staff=True)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    login_method = models.CharField(default='email', max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    name = models.CharField(default='닉네임', max_length=50, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    about = models.TextField(default='자신을 소개해주세요 :)', null=True, blank=True)
    gnere = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follower(models.Model):
    target_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target_id')
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_id')
    created_at = models.DateTimeField(auto_now_add=True)
