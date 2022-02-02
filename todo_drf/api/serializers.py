from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `Task` instance, given the validated data.
        """
        return Task.objects.create(**validated_data)
