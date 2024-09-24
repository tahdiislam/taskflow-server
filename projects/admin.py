from django.contrib import admin
from .models import Project, ProjectRole

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectRole)