from rest_framework import serializers
from object_detection_model.serializer.serializers import ObjectDetectionModelSerializer
from project.models import Project


class ProjectModelSerializer(serializers.ModelSerializer):
    object_detection_model_name = ObjectDetectionModelSerializer(read_only=True)

    class Meta:
        model = Project
        # fields = ['id',
        #           'object_detection_model_name_id',
        #           'project_name',
        #           'object_detection_model_name'
        #           ]
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
