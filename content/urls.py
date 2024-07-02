

from django.urls import path
from .views import UploadFeed,Main

urlpatterns = [
    path("upload", UploadFeed.as_view()),
    path('main', Main.as_view())
]
