# learning_vid\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('learning_vid/', views.learning_vid, name='videos'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
