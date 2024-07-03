from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from user_profiles.views import upload_resume, profile, home


urlpatterns = [
    path('', home, name='home'),
    path('upload_resume/', upload_resume, name='upload_resume'),
    path('profile/', profile, name='profile'),
]