# Generated by Django 4.1.7 on 2023-04-04 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="object_detection_model_name_id",
            new_name="object_detection_model_name",
        ),
    ]