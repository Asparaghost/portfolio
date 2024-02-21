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
    path('sample', views.sample, name='sample'),
]