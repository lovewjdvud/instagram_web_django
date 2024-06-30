from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class USer(AbstractBaseUser):
    # 프로필 사진
    # 유저 닉네임
    # 유저 이름
    # 유저 이메일 주소
    # 유저 비번 -> 디폴트



    profile_image = models.TextField()
    nickname = models.CharField(max_length=24,unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'
    class Meta:
        db_table = 'User'