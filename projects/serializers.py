from rest_framework import serializers
from .models import Project, ProjectRole

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # exclude = ['team_members', 'end_date']
        fields = '__all__'
        read_only_fields = ['is_finished']