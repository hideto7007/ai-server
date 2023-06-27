from django.urls import path
from rest_framework import routers

from evals.views import (
    LearningModelDownloadAPIView
)

# API
urlpatterns = [
    path("learning_model_list/", LearningModelDownloadAPIView.as_view()),
    # path("object_detection_model_delete", ObjectDetectionModelDeleteAPIView.as_view()),
    # path("object_detection_model_update", ObjectDetectionModelPostListAPIView.as_view()),
]