# Generated by Django 4.1.7 on 2023-05-31 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "project",
            "0002_rename_object_detection_model_name_id_project_object_detection_model_name",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="object_detection_model_name",
            new_name="object_detection_model_name_id",
        ),
    ]