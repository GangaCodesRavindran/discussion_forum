from django.urls import path
from . import views

urlpatterns = [
    path('my_video/', views.my_video, name='my_video'),
]
