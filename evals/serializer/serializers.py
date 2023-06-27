from rest_framework import serializers
from evals.models import LearningImage


class LearningImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningImage
        fields = "__all__"