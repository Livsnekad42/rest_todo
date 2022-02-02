from django.urls import path
from .views import ApiOverview

urlpatterns = [
    path('', ApiOverview.as_view(), name='api-overview'),
]
