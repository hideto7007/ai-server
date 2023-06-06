from django.urls import path
from rest_framework import routers

from project.views import (
    ProjectlListAPIView,
    ProjectPostListAPIView,
    ProjectDeleteAPIView
)

# API
urlpatterns = [
    path("project_list/", ProjectlListAPIView.as_view()),
    path("project_create_or_update/", ProjectPostListAPIView.as_view()),
    path("project_delete/", ProjectDeleteAPIView.as_view()),
]