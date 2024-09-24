from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'