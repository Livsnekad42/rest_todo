from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


class TaskOverview(APIView):
    serializerClass = TaskSerializer

    def get(self, request):
        tasks = Task.objects.all()
        serializer = self.serializerClass(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskCreateView(APIView):

    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_200_OK)

        except():
            return Response({'errors': {
                "detail": [('Invalid task.')]
            }}, status=status.HTTP_400_BAD_REQUEST)


def task_form(request):
    return render(request, 'api/main.html')