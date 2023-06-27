from django.db import models
from project.models import Project


class LearningImage(models.Model):
    """学習させる画像及び学習後の画像情報モデル"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
