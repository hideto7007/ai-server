from django.urls import path
from rest_framework import routers

from object_detection_model.views import (
    ObjectDetectionModelListAPIView,
    ObjectDetectionModelDeleteAPIView,
    ObjectDetectionModelPostListAPIView
)

# API
urlpatterns = [
    path("object_detection_model_list/", ObjectDetectionModelListAPIView.as_view()),
    path("object_detection_model_delete", ObjectDetectionModelDeleteAPIView.as_view()),
    path("object_detection_model_update", ObjectDetectionModelPostListAPIView.as_view()),
]