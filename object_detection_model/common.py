from object_detection_model.models import ObjectDetectionModel
from project.models import Project
from evals.models import LearningImage
from object_detection_model.serializer.serializers import ObjectDetectionModelSerializer
from django.db.models import Q
import datetime
from dateutil import tz
import pandas as pd
import json
import os
import shutil

from common.common import (
    value_check,
    dbvalue_to_str,
    datetime_valid_check,
    valid_int,
    valid_date,
    int_replace,
    each_items_valid,
    valid_request_check

)
from const.const import ObjectDetectionModelColumn, RequestDateType, PathList


def get_object_detection_model_list():
    """
        物体検知モデルデータ取得

    """

    result = []
    object_detection_model_request = ObjectDetectionModel.objects.all().order_by('-created_at')

    for res in ObjectDetectionModelSerializer(object_detection_model_request, many=True).data:
        result.append(
            {
                ObjectDetectionModelColumn.ID.value: dbvalue_to_str(res["id"]),
                ObjectDetectionModelColumn.OBJECT_DETECTION_MODEL_NAME.value: dbvalue_to_str(
                    res["object_detection_model_name"]),
            }
        )

    return result


def update_request(queryset, serializer, key_id, id_value, request):
    """データ更新、登録"""

    timestamp = 1337000000

    flag = True

    filter_dict = {
        key_id: str(id_value),
    }

    result = []
    save_query = queryset.objects.filter(**filter_dict).first()
    query_request = request.data[RequestDateType.ENTRY_DATA.value]
    for res in query_request:
        res["object_detection_model_name"] = res["name"]
        res["update_user"] = str(request.user)
        res["delete_flag"] = "0"
        res["created_at"] = datetime.datetime.fromtimestamp(timestamp, tz=tz.gettz('Asia/Tokyo'))

        if save_query is None:
            # user_idが異なる場合新規登録処理
            serializer = serializer(data=res)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            elif not serializer.save():
                result = "DB登録失敗"
            else:
                result = "DB登録内容エラー"

        else:
            # user_idが同一の場合は更新処理
            serializer = serializer(instance=save_query, data=res)
            flag = False
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            elif not serializer.save():
                result = "更新失敗"
            else:
                result = "更新内容エラー"

    return result, flag


def update_object_detection_model_name_request(request):
    """物体検知モデル名データの登録、更新"""
    result = valid_request_check(request)
    if len(result) > 0:
        return result

    name_list = []

    print(request.data["data"][0][RequestDateType.ID.value])

    before_model_name = ObjectDetectionModel.objects.filter(id=request.data["data"][0][RequestDateType.ID.value])
    if len(before_model_name) != 0:
        name_list.append(before_model_name[0])

    result, flag = update_request(ObjectDetectionModel,
                                  ObjectDetectionModelSerializer,
                                  ObjectDetectionModelColumn.ID.value,
                                  request.data["data"][0][RequestDateType.ID.value],
                                  request)

    after_model_name = ObjectDetectionModel.objects.filter(id=request.data["data"][0][RequestDateType.ID.value])
    if len(after_model_name) != 0:
        name_list.append(after_model_name[0])
    project_name = Project.objects.filter(object_detection_model_name=request.data["data"][0][RequestDateType.ID.value])
    # 各オブジェクトの特定のフィールドの値を取得
    values = [obj.project_name for obj in project_name]

    print(os.listdir("./evals/model"))

    if not flag:
        for path in PathList.path_list.value:
            for project in values:
                before_path = path + "/" + str(name_list[0]) + "/" + project
                after_path = path + "/" + str(name_list[1]) + "/" + project

                shutil.move(before_path, after_path)

                # 削除しない代わりに、画像情報DB内のパスを一部更新出来るようにする
                path_name = LearningImage.objects.filter(file_path__icontains=before_path)

                if len(path_name) >= 1:

                    new_path_name = str(path_name[0]).replace(str(name_list[0]), str(name_list[1]))

                    for obj in path_name:
                        obj.file_path = new_path_name
                        obj.save()

        # いらなくなったディレクトリ削除
        for path in PathList.path_list.value:
            if os.path.isdir(path + "/" + str(name_list[0])):
                os.rmdir(path + "/" + str(name_list[0]))

    return result
