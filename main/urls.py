from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('post_question/', views.post_question, name='post_question'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
]