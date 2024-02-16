from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    lang_id = models.AutoField(primary_key=True)
    lang_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return self.lang_name
    
    class Meta:
        db_table = "language"


class Project(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_name = models.CharField(max_length=100)
    proj_img = models.ManyToManyField('ProjectImage')
    proj_desc = models.TextField()
    proj_lang = models.ManyToManyField(Language)
    proj_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return self.proj_name
    
    class Meta:
        db_table = "projects"


class ProjectImage(models.Model):
    proj_img = models.ImageField(upload_to='proj_images/')