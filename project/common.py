from project.models import Project
from object_detection_model.models import ObjectDetectionModel
from project.serializer.serializers import ProjectModelSerializer, ProjectSerializer
from django.db.models import Q
import datetime
from dateutil import tz
import pandas as pd
import json

from common.common import (
    value_check,
    dbvalue_to_str,
    datetime_valid_check,
    valid_int,
    valid_date,
    int_replace,
    each_items_valid,
    valid_request_check,
    get_best_new_id

)
from const.const import ObjectDetectionModelColumn, RequestDateType, ProjectColumn


def get_project_model_list(model_name, id_str):
    """
        プロジェクトデータ取得
    """

    result = []
    project_object_detection_model_request = Project.objects.select_related('object_detection_model_name')\
        .filter(object_detection_model_name__object_detection_model_name=model_name,
                object_detection_model_name_id=id_str)

    for res in ProjectModelSerializer(project_object_detection_model_request, many=True).data:
        result.append(
            {
                ProjectColumn.ID.value: dbvalue_to_str(res["id"]),
                ProjectColumn.PROJECT_NAME.value: dbvalue_to_str(res["project_name"]),
                ObjectDetectionModelColumn.OBJECT_DETECTION_MODEL_NAME_ID.value: dbvalue_to_str(
                    [x for x in
                     [v for k, v in res["object_detection_model_name"].items()
                      if k == "id"]][0]),
                ObjectDetectionModelColumn.OBJECT_DETECTION_MODEL_NAME.value: dbvalue_to_str(
                    [x for x in
                     [v for k, v in res["object_detection_model_name"].items()
                      if k == "object_detection_model_name"]][0]),
            }
        )

    return result


def update_request(queryset, serializer, key_id, id_value_flag, request, user):
    """
        データ更新、登録

        queryset(queryObject): モデル,
        serializer(json): モデルシリアライザー,
        key_id(str): オブジェクトのキー,
        id_value_flag(str): 各オブジェクトのid値,
        request(object): 各オブジェクト,
        user(str): ログインユーザー情報
    """

    timestamp = 1337000000

    # id_valueが0の場合、一番最新のidに対してプラス1して、id取得する(新規作成)
    # 更新の場合、id_valueにそのままid_value_flagを代入する
    if id_value_flag == "0":
        id_value = str(get_best_new_id(Project, ProjectModelSerializer) + 1)
    else:
        id_value = id_value_flag

    filter_dict = {
        key_id: str(id_value),
    }

    result = []
    save_query = queryset.objects.filter(**filter_dict).first()
    request["update_user"] = str(user)
    request["delete_flag"] = "0"
    request["created_at"] = datetime.datetime.fromtimestamp(timestamp, tz=tz.gettz('Asia/Tokyo'))

    if save_query is None:
        # user_idが異なる場合新規登録処理
        print("create")
        print(request)
        serializer = serializer(data=request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        elif not serializer.save():
            result = "DB登録失敗"
        else:
            result = "DB登録内容エラー"

    else:
        # user_idが同一の場合は更新処理
        print("update")
        print(request)
        serializer = serializer(instance=save_query, data=request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        elif not serializer.save():
            result = "更新失敗"
        else:
            result = "更新内容エラー"

    return result


def update_project_request(request):
    """プロジェクトデータの登録、更新"""
    result = valid_request_check(request)
    if len(result) > 0:
        return result

    for val in request.data["data"]:
        result = update_request(Project,
                                ProjectSerializer,
                                ProjectColumn.ID.value,
                                val[RequestDateType.ID.value],
                                val,
                                request.user)

    return result
