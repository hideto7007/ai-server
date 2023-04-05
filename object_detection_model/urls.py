from django.urls import path
from rest_framework import routers

from object_detection_model.views import ObjectDetectionModelListAPIView

# API
urlpatterns = [
    path("object_detection_model_list/", ObjectDetectionModelListAPIView.as_view()),
]