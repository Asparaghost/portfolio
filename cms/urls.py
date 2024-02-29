from django.contrib import admin
from django.contrib.auth import views as authentication_views
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project_apps', views.project_apps, name='project_apps'),
    path('project_graphic_arts', views.project_graphics, name='project_graphics'),
    path('project_logos', views.project_logos, name='project_logos'),

    path('login',authentication_views.LoginView.as_view(template_name='cms/login.html'), name='login'),
    path('logout',authentication_views.LogoutView.as_view(template_name='cms/login.html'), name='logout'),

    path('project/<str:proj_id>/',views.details, name='details'),

    path('dashboard/add_Project/',views.add_proj, name='add_proj'),
    path('dashboard/delete/<str:proj_id>/', views.delete_proj, name='delete_proj'),

    path('dashboard/add_Language/',views.add_lang, name='add_lang'),
    path('dashboard/edit/<str:lang_id>/', views.edit_lang, name='edit_lang'), 
    path('dashboard/delete/<str:lang_id>/', views.delete_lang, name='delete_lang'), 
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('user', views.user, name='user'),
]