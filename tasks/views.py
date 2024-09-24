from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        priority = self.request.query_params.get('priority')
        if priority is not None:
            queryset = queryset.filter(priority=priority)
        assigned_to = self.request.query_params.get('assigned_to')
        if assigned_to is not None:
            queryset = queryset.filter(assigned_to=assigned_to)
        due_date = self.request.query_params.get('due_date')
        if due_date is not None:
            queryset = queryset.filter(due_date=due_date)
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset