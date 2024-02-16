from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *

# Create your views here.
def index(request):
    projects = Project.objects.all()  
    context = {
        'projects':projects
    }
    return render(request, "cms/index.html", context)

def projects(request):
    projects = Project.objects.all()  
    context = {
        'projects':projects
    }
    return render(request, "cms/projects.html", context)