# Generated by Django 4.1.7 on 2023-03-30 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("object_detection_model", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=20)),
                ("delete_flag", models.IntegerField()),
                ("update_user", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField()),
                (
                    "object_detection_model_name_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="object_detection_model.objectdetectionmodel",
                    ),
                ),
            ],
        ),
    ]