# disc_forum\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('forum/<int:pk>/', views.question_detail, name='question_detail'),
    path('delete_question/<int:pk>/', views.delete_question_detail, name='delete_question_detail'),
    path('update_question/<int:pk>/', views.update_question_detail, name='update_question_detail'),
    path('delete_answer/<int:pk>/', views.delete_answer, name='delete_answer'),
    path('update_answer/<int:pk>/', views.update_answer, name='update_answer'),
    path('post_question/', views.post_question, name='post_question'),
]
