from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self, request):
        feedList = Feed.objects.all().order_by("-id")
        print(feedList)
        return render(request, "instagram/main.html",context=dict(feeds=feedList))
