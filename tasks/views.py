from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = None

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

class TaskUpdateViewSet(APIView):
    def patch(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskUpdateSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)