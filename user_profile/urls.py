
from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profiles_view, name='profiles'),
    path('delete_skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('update_skill/<int:skill_id>/', views.update_skill, name='update_skill'),
    path('add_skill/<int:user_id>/', views.add_skill_view, name='add_skill'),
    path('profiles/<int:user_id>/edit/', views.edit_competency_page, name='edit-competency-page'),
    path('export_report/', views.export_report, name='export_report'),
]
