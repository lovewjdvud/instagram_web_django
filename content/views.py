from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
import os
from instagram_web.settings import MEDIA_ROOT

# Create your views here.
class Main(APIView):
    def get(self, request):
        feedList = Feed.objects.all().order_by("-id")
        print('로그인 사용자 : ',request.session.get('email'))
        email = request.session.get('email')

        if email is None:
            return render(request, "user/login.html",)

        user = Feed.objects.filter(email=email)

        if user is None:
            return render(request, "user/login.html",)

        return render(request, "instagram/main.html",context=dict(feeds=feedList,user=user))

class Upload(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id 