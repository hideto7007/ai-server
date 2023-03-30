from django.db import models

# Create your models here.


class Project(models.Model):
    id = models.UUIDField(primary_key=True)
    object_detection_model_name_id = models.IntegerField()
    project_name = models.CharField(max_length=20)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project'
