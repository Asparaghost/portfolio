from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import *

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

def dashboard(request):
    projects = Project.objects.all()  
    languages = Language.objects.all()
    context = {
        'projects':projects,
        'languages':languages,
    }
    return render(request, "cms/admin/dashboard.html", context)

def add_lang(request):
    if request.method == "POST":  
        form = LanguageForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.created_by = request.user
                instance.save()
                form.save_m2m()
                return redirect('/dashboard')  
            except:  
                pass
    else:  
        form = LanguageForm()  
    return render(request,'cms/admin/add_lang.html',{'form':form})  

def edit_lang(request, lang_id):  
    language = Language.objects.get(lang_id=lang_id)  
    form = LanguageForm(instance = language)  
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance = language)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)  
                instance.save()
                form.save_m2m()
                return redirect('/dashboard')  
            except:  
                pass
    return render(request, 'cms/admin/edit_lang.html', {'form':form})  

def delete_lang(request, lang_id):  
    language = Language.objects.get(lang_id=lang_id)  
    language.delete()  
    return redirect("/dashboard")  