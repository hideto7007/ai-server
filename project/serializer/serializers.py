from rest_framework import serializers
from object_detection_model.serializer.serializers import ObjectDetectionModelSerializer
from project.models import Project


class ProjectModelSerializer(serializers.ModelSerializer):
    object_detection_model_name = ObjectDetectionModelSerializer()

    class Meta:
        model = Project
        # fields = ['id',
        #           'object_detection_model_name_id',
        #           'project_name',
        #           'object_detection_model_name'
        #           ]
        fields = "__all__"
