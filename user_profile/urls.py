# from django.urls import path
# from . import views
# from .views import profiles_view, add_skill_view, UserProfileList, UserProfileDetail, UserSkillCreate, UserSkillUpdateDelete, profiles_page, edit_competency_page

# urlpatterns = [
#     # path('profiles/', profiles_page, name='profiles-page'),
#     path('profiles/', profiles_view, name='profiles'),
#     path('delete_skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
#     path('update_skill/<int:skill_id>/', views.update_skill, name='update_skill'),
#     path('add_skill/<int:user_id>/', add_skill_view, name='add_skill'),
#     path('profiles/<int:user_id>/edit/', edit_competency_page, name='edit-competency-page'),
#     path('api/profiles/', UserProfileList.as_view(), name='userprofile-list'),
#     path('api/profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
#     path('api/skills/', UserSkillCreate.as_view(), name='userskill-create'),
#     path('api/skills/<int:pk>/', UserSkillUpdateDelete.as_view(), name='userskill-update-delete'),
#     path('export_report/', views.export_report, name='export_report'),
#     path('profile/profiles/report/', views.generate_report, name='generate_report'),

# ]


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
