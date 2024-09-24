from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.CASCADE)
    team_members = models.ManyToManyField(User, through='ProjectRole', related_name='projects')
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Member', 'Member')
]

# Create your models here.
class ProjectRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')
    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return self.user.username