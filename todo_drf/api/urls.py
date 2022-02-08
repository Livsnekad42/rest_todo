from django.urls import path
from .views import TaskOverview, task_form, TaskCreateView

urlpatterns = [
    path('', TaskOverview.as_view(), name='api-overview'),
    path('task-form', task_form, name='task-form'),
    path('task-create', TaskCreateView.as_view(), name='task-form'),
]
