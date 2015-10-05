from rest_framework import serializers
from work.models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'shortname', 'description', 'owner', 'start_date', 'end_date', 'is_active')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'project', 'start_date', 'end_date', 'worker', 'completed')
