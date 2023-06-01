from django.urls import path
from rest_framework import routers

from project.views import (
    ProjectlListAPIView
)

# API
urlpatterns = [
    path("project_list/", ProjectlListAPIView.as_view()),
]