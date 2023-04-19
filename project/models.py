from django.db import models
from object_detection_model.models import ObjectDetectionModel

from django.utils import timezone
import uuid


class Project(models.Model):
    """物体検知各プロジェクトモデル"""

    object_detection_model_name = models.ForeignKey(ObjectDetectionModel, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.project_name

