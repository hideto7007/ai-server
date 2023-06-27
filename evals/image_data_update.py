import os
import sys
import csv
from typing import Any, List, Union, Dict
from datetime import datetime as dt
from datetime import timedelta as td
from dateutil import tz
import random
import logging


class ScriptHandler:
    def __init__(self, file_path: str, update_user: str) -> None:
        self.file_path: str = file_path
        self.update_user = update_user
        self.result = [[], [], []]


    def image_db_update(self) -> None:
        """inputに格納されていてまだDBに登録されてない画像を登録する"""

        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s")

        timestamp = dt.now().timestamp()

        for input_path in os.listdir(self.file_path):
            for projects in os.listdir(self.file_path + input_path):
                for file in os.listdir(self.file_path + input_path + "/" + projects):
                    self.result[0].append(projects)
                    self.result[1].append(self.file_path + input_path + "/" + projects + "/")
                    self.result[2].append(file)

        get_id = LearningImage.objects.all().order_by("-id").first()

        for project_name, file_path, file_name in zip(self.result[0], self.result[1], self.result[2]):
            query_search = LearningImage.objects.filter(file_path=file_path, file_name=file_name)
            get_project_name = Project.objects.filter(project_name=project_name)
            if len(query_search) == 0:
                res = {
                    "id": get_id.id + 1,
                    "file_name": file_name,
                    "file_path": file_path,
                    "delete_flag": "0",
                    "update_user": self.update_user,
                    "created_at": dt.fromtimestamp(timestamp, tz=tz.gettz('Asia/Tokyo')),
                    "project": get_project_name[0].id
                }

                serializer = LearningImageSerializer(data=res)
                if serializer.is_valid():
                    # バリデーションが成功した場合の処理
                    serializer.save()  # オブジェクトを保存
                    # 必要な処理を実行
                    logging.critical("DB success save")
                else:
                    # バリデーションが失敗した場合の処理
                    errors = serializer.errors
                    logging.error(errors)


class ScriptObject:
    def __init__(self, script_handler: ScriptHandler) -> None:
        self.script_handler: ScriptHandler = script_handler

    def trigger_event(self) -> None:
        """トリガーイベント発生"""
        self.script_handler.image_db_update()


if __name__ == "__main__":
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    django.setup()

    from evals.models import LearningImage
    from project.models import Project
    from evals.serializer.serializers import LearningImageSerializer
    from django.db.models import Q
    from django.db.models.query import QuerySet

    # パラメータ引数
    path = "../evals/input/"
    user = "tsuzuki"

    script = ScriptHandler(path, user)

    script_object = ScriptObject(script)

    script_object.trigger_event()
