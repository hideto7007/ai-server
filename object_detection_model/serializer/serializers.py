from rest_framework import serializers
from object_detection_model.models import ObjectDetectionModel


class ObjectDetectionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjectDetectionModel
        fields = "__all__"