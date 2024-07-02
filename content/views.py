from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from user.models import User
import os
from instagram_web.settings import MEDIA_ROOT

# Create your views here.
class Main(APIView):
    def get(self, request):
        feedList = Feed.objects.all().order_by("-id")
        # print('로그인 사용자 : ',request.session.get('email'))
        email = request.session.get('email')
        print('로그인 사용자 : 3 ', request.session.get('email'))
        if email is None:
            return render(request, "user/login.html",)
        print('로그인 사용자 1: ', request.session.get('email'))
        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html",)
        print('로그인 사용자 2: ', request.session.get('email'))
        return render(request, "instagram/main.html",context=dict(feeds=feedList,user=user))

class UploadFeed(APIView):
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']

        uuid_name = 