from django.contrib import admin
from .models import Task, Comment, ActivityLog, Notification

# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(ActivityLog)
admin.site.register(Notification)