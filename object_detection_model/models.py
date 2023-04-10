from django.db import models

from django.utils import timezone
import uuid


class ObjectDetectionModel(models.Model):
    """物体検知モデル"""

    object_detection_model_name = models.CharField(unique=True, max_length=20)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.object_detection_model_name


