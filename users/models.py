from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ADMIN = 'ADMIN'
MANAGER = 'MANAGER'
MEMBER = 'MEMBER'

ROLE_CHOICES = [
        (MEMBER, 'Member'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
        ]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=MEMBER)
    profile_picture = models.ImageField(upload_to="users/images", blank=True, null=True)
    task_completed = models.PositiveIntegerField(default=0)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)