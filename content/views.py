from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self, request):
        feedList = Feed.objects.all().order_by("-id")
        print(feedList)
        return render(request, "instagram/main.html",context=dict(feeds=feedList))

class Upload(APIView):
    def post(self, request):
        # file = request.FILES['file']
        # image = request.FILES['image']
        # content = request.FILES['content']
        # user_id = request.FILES['user_id']
        # profile_image = request.FILES['profile_image']
        content = request.data.get('content')
        if content is None:
            content = '암것도 없어'
        print('ㅋㅋ' + content)

        return Response(status=200)