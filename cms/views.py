from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    projects = Project.objects.all()  
    informations = Information.objects.all() 
    context = {
        'projects':projects,
        'informations':informations
    }
    return render(request, "cms/index.html", context)


def project_apps(request):
    projects = Project.objects.filter(proj_type='Application')    
    context = {
        'projects':projects
    }
    return render(request, "cms/projects_app.html", context)


def project_graphics(request):
    projects = Project.objects.filter(proj_type='Graphic Art')  
    context = {
        'projects':projects
    }
    return render(request, "cms/projects_graphic.html", context)


def project_logos(request):
    projects = Project.objects.filter(proj_type='Logo')  
    context = {
        'projects':projects
    }
    return render(request, "cms/projects_logo.html", context)


def details(request, proj_id):
    project = Project.objects.get(proj_id=proj_id)
    project_lang = project.proj_lang.all()
    context = {
        'project' : project,
        'project_lang' : project_lang,
    }
    return render(request, "cms/details.html", context)


def login(request):
    return render(request, "cms/login.html")

def sample(request):
    return render(request, "cms/admin/dashboard.html")