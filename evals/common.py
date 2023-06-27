import os
from typing import Any, Type, Dict
from .models import LearningImage
from .serializer.serializers import LearningImageSerializer
from django.db.models import Q
from django.db.models.query import QuerySet


class EventHandler:
    def __init__(self, model: str, project: str) -> None:
        self.path = ["./evals/model", "./evals/input", "./evals/output"]
        self.model = model
        self.project = project
        # パスを結合
        self.joined_path = self.path[0] + "/" + self.model + "/" + self.project + "/"
        self.joined_image_input_path = self.path[1] + "/" + self.model + "/" + self.project + "/"
        self.joined_image_output_path = self.path[2] + "/" + self.model + "/" + self.project + "/"

    def get_pth_file(self) -> Dict[int, str]:
        """各モデルのpthファイル取得"""
        result = {}

        for idx, val in enumerate(os.listdir(self.joined_path)):
            result[idx] = val

        return result

    def get_input_image_file(self) -> Dict[int, str]:
        """各画像パス一覧取得"""
        result = {}

        learning_image_query = LearningImage.objects. \
            filter(file_path__icontains=self.model). \
            filter(file_path__icontains=self.project). \
            filter(file_path__icontains=self.path[1])

        for idx, res in enumerate(LearningImageSerializer(learning_image_query, many=True).data):
            result[idx] = res["file_path"] + res["file_name"]

        return result


    def get_output_image_file(self) -> Dict[int, str]:
        """各学習後の画像パス一覧取得"""
        result = {}

        learning_image_query = LearningImage.objects. \
            filter(file_path__icontains=self.model). \
            filter(file_path__icontains=self.project). \
            filter(file_path__icontains=self.path[2])

        for idx, res in enumerate(LearningImageSerializer(learning_image_query, many=True).data):
            result[idx] = res["file_path"] + res["file_name"]

        return result


class EventObject:
    def __init__(self, event_handler: EventHandler) -> None:
        self.event_handler = event_handler

    def get_pth_file_trigger_event(self) -> Dict[int, str]:
        return self.event_handler.get_pth_file()

    def get_input_image_file_trigger_event(self) -> Dict[int, str]:
        return self.event_handler.get_input_image_file()

    def get_output_image_file_trigger_event(self) -> Dict[int, str]:
        return self.event_handler.get_output_image_file()
