from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectImage)
admin.site.register(Information)