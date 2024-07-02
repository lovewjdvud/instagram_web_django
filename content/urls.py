

from django.urls import path
from .views import UploadFeed,Main

urlpatterns = [
    path("upload", UploadFeed.