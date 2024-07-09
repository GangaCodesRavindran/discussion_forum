from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('forum/<int:pk>/', views.question_detail, name='question_detail'),
    path('post_question/', views.post_question, name='post_question'),
]
