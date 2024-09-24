from django.shortcuts import render
from .models import Project, ProjectRole
from .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save()
        ProjectRole.objects.create(user=project.created_by, project=project, role='Admin')