from django.db import models

from django.utils import timezone
import uuid

# Create your models here.


class ObjectDetectionModel(models.Model):
    """物体検知モデル"""

    id = models.UUIDField(primary_key=True)
    project_name_id = models.IntegerField()
    object_detection_model_name = models.CharField(unique=True, max_length=20)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'object_detection_model'
