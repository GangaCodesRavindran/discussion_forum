from django.urls import path, include
from . import views
from .views import ProfileView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profiles/', ProfileView.as_view(), name='profiles'),
]
    
