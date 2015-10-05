from rest_framework import serializers
from work.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'shortname', 'description', 'owner', 'start_date', 'end_date', 'is_active')
