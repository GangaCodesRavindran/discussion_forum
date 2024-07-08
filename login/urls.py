from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('forum_redirect/', views.forum_redirect, name='forum_redirect'),
    path('learning_vid/', views.videos_redirect, name='videos_redirect'),
    path('login/', views.user_login, name='user_login'),
]
