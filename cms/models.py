from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Information(models.Model):
    info_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    github_url = models.URLField(max_length=255, blank=True, null=True)
    email_add = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    class Meta:
        db_table = "personal_information"

class Language(models.Model):
    lang_id = models.AutoField(primary_key=True)
    lang_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return self.lang_name
    
    class Meta:
        db_table = "languages"


class Project(models.Model):
    APPLICATION = 'Application'
    GRAPHIC_ART = 'Graphic Art'
    LOGO = 'Logo'

    CHOICE_PROJECT = (
        (APPLICATION, 'Application'),
        (GRAPHIC_ART, 'Graphic Art'),
        (LOGO, 'Logo'),
    )
    proj_id = models.AutoField(primary_key=True)
    proj_name = models.CharField(max_length=100)
    proj_type = models.CharField(max_length=20, choices=CHOICE_PROJECT, default=APPLICATION)
    proj_img = models.ManyToManyField('ProjectImage', blank=True)
    proj_desc = models.TextField()
    proj_lang = models.ManyToManyField(Language, blank=True)
    proj_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return self.proj_name
    
    class Meta:
        db_table = "projects"


class ProjectImage(models.Model):
    proj_img = models.ImageField(upload_to='proj_images/')

    def __str__(self):
        return self.proj_img.name
    
    class Meta:
        db_table = "project_images"