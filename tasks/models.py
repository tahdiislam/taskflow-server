from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.

STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=200,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='Low')
    # due_date = models.DateField()
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='activity_logs', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message