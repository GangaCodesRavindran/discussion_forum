from django.shortcuts import render
from .models import MyVideo

def my_video(request):
    myvideo=MyVideo.objects.all()
    return render(request, "my_video/my_video.html",{"myvideo":myvideo})