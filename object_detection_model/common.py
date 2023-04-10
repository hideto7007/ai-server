from object_detection_model.models import ObjectDetectionModel
from object_detection_model.serializer.serializers import ObjectDetectionModelSerializer
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
    int_replace
)
from const.const import ObjectDetectionModelColumn, RequestDateType


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


def each_items_valid(key, value):
    """各項目バリデーションチェック"""

    result = []
    # 全て必須項目
    required = True
    if key == "object_detection_model_name":
        if not valid_date(value, required):
            result.append("物体検知モデル名")

    return result


def valid_request_check(request):
    """登録データへの妥当性チェック"""

    result = []
    object_detection_model_name_request = request.data[RequestDateType.ENTRY_DATA.value][0]

    for key, val in object_detection_model_name_request.items():
        valid_items = each_items_valid(key, val)
        result.append(valid_items)

    if len(result) > 0:
        error_list = ['{0}行目で、{1}項目でのバリデーションエラー'.format(idx + 1, vals)
                      for idx, val in enumerate(result) for vals in val]
        return error_list

    return result


def update_request(queryset, serializer, key_id, id_value, request):
    """データ更新、登録"""

    query_request = request.data[RequestDateType.ENTRY_DATA.value]

    timestamp = 1337000000

    for data in query_request:
        existing_data = data.get("id", None)

        filter_dict = {
            key_id: request.data.get(id_value, ""),
        }

        if existing_data is not None:
            filter_dict["id"] = existing_data

        result = []
        save_query = queryset.objects.filter(**filter_dict).first()
        query = serializer(queryset.objects.filter(**filter_dict), many=True).data
        query_request = request.data[RequestDateType.ENTRY_DATA.value]
        for res in query_request:
            res["object_detection_model_name"] = res["name"]
            res["update_user"] = str(request.user)
            res["delete_flag"] = "0"
            res["created_at"] = datetime.datetime.fromtimestamp(timestamp, tz=tz.gettz('Asia/Tokyo'))

            if len(query) == 0:
                # user_idが異なる場合新規登録処理
                serializer = serializer(data=res)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                elif not serializer.save():
                    result = "DB登録失敗"
                else:
                    result = "DB登録内容エラー"

            elif str(query[0]["id"]) == existing_data:
                # user_idが同一の場合は更新処理
                serializer = serializer(instance=save_query, data=res)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                elif not serializer.save():
                    result = "更新失敗"
                else:
                    result = "更新内容エラー"

        return result


def update_object_detection_model_name_request(request):
    """物体検知モデル名データの登録、更新"""
    result = valid_request_check(request)
    if len(result) > 0:
        return result

    # result = update_request(ObjectDetectionModel,
    #                         ObjectDetectionModelSerializer,
    #                         ObjectDetectionModelColumn.ID.value,
    #                         RequestDateType.ID.value,
    #                         request)

    result = update_request(ObjectDetectionModel,
                            ObjectDetectionModelSerializer,
                            ObjectDetectionModelColumn.ID.value,
                            RequestDateType.ID.value,
                            request)

    return result
