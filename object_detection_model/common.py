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
    int_replace,
    each_items_valid,
    valid_request_check

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


def update_request(queryset, serializer, key_id, id_value, request):
    """データ更新、登録"""

    timestamp = 1337000000

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

    result = update_request(ObjectDetectionModel,
                            ObjectDetectionModelSerializer,
                            ObjectDetectionModelColumn.ID.value,
                            request.data["data"][0][RequestDateType.ID.value],
                            request)

    return result
