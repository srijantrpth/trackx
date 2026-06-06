from rest_framework import serializers
from .models import Project, Task
class ProjectSerializer(serializers.ModelSerializer):


    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['owner']
    def validate_name(self, value):
        if len(value)<3:
            raise serializers.ValidationError('Project name must be at least 3 characters long!')
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title','status','project','created_at']

