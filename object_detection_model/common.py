from object_detection_model.models import ObjectDetectionModel
from object_detection_model.serializer.serializers import ObjectDetectionModelSerializer
from django.db.models import Q
import datetime
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
# from const.const import IncomeForecastColumnName, RequestDateType, ApiResultKind


def get_object_detection_model_list():
    """
        物体検知モデルデータ取得

    """

    # if not value_check(model_id_str):
    #     result = "idが不正です"
    #     return result
    #
    # # フィルター条件を辞書型で格納
    # filter_dict = {
    #     "id__lte": model_id_str,
    #     "delete_flag": "0"
    # }

    # 日付範囲指定処理 %Y-%m-%d %H:%M:%S.%f
    # try:
    #     if start_date and not end_date:
    #         start_date = datetime.datetime.strptime(start_date + " 00:00:00", '%Y-%m-%d %H:%M:%S')
    #         filter_dict["payment_date__gte"] = start_date
    #     elif end_date and not start_date:
    #         end_date = datetime.datetime.strptime(end_date + " 23:59:59", '%Y-%m-%d %H:%M:%S')
    #         filter_dict["payment_date__lte"] = end_date
    #     elif start_date and end_date:
    #         start_date = datetime.datetime.strptime(start_date + " 00:00:00", '%Y-%m-%d %H:%M:%S')
    #         filter_dict["payment_date__gte"] = start_date
    #         end_date = datetime.datetime.strptime(end_date + " 23:59:59", '%Y-%m-%d %H:%M:%S')
    #         filter_dict["payment_date__lte"] = end_date
    # except TypeError:
    #     pass

    result = []
    object_detection_model_request = ObjectDetectionModel.objects.all().order_by('-created_at')

    for res in ObjectDetectionModelSerializer(object_detection_model_request, many=True).data:
        result.append(
            {
                "id": dbvalue_to_str(res["id"]),
                "object_detection_model_name": dbvalue_to_str(res["object_detection_model_name"]),
            }
        )

    return result


# def get_old_date_list(user_id_str):
#     """年収推移の中から最も古い日付取得"""
#
#     """
#         年収推移データ取得
#
#         user_id_str: str
#             userid
#     """
#
#     if not value_check(user_id_str):
#         result = "idが不正です"
#         return result
#
#     # フィルター条件を辞書型で格納
#     filter_dict = {
#         "user_id": user_id_str,
#         "delete_flag": "0"
#     }
#
#     result = []
#     old_date = IncomeForecastData.objects.filter(**filter_dict).order_by('payment_date').first()
#     if old_date is not None:
#         result.append(
#             {
#                 IncomeForecastColumnName.PAYMENT_DATE.value: dbvalue_to_str(old_date.payment_date)
#             }
#         )
#     else:
#         result.append(
#             {
#                 IncomeForecastColumnName.PAYMENT_DATE.value: datetime.datetime.now().strftime('%Y-%m-%d')
#             }
#         )
#
#     return result
#
#
# def get_total_incme_date_list(user_id_str):
#     """各年ごとの年収取得"""
#
#     """
#         各年ごとの年収データ取得
#
#         user_id_str: str
#             userid
#     """
#
#     if not value_check(user_id_str):
#         result = "idが不正です"
#         return result
#
#     # フィルター条件を辞書型で格納
#     filter_dict = {
#         "user_id": user_id_str,
#         "delete_flag": "0"
#     }
#
#     result = []
#     income_date = IncomeForecastData.objects.filter(**filter_dict).order_by('payment_date')
#     for res in IncomeForecastDataSerializer(income_date, many=True).data:
#         result.append(
#             {
#                 IncomeForecastColumnName.PAYMENT_DATE.value: dbvalue_to_str(res["payment_date"][:4]),
#                 IncomeForecastColumnName.TOTAL_AMOUNT.value: int_replace(res["total_amount"]),
#                 IncomeForecastColumnName.DEDUCTION_AMOUNT.value: int_replace(res["deduction_amount"]),
#                 IncomeForecastColumnName.TAKE_HOME_AMOUNT.value: int_replace(res["take_home_amount"]),
#             }
#         )
#     agg_result = []
#     df = pd.json_normalize(result)
#
#     if len(df) != 0:
#         sum_income = df.groupby(['payment_date']).sum()
#         income_dict = sum_income.to_dict()
#         labels = [i for i in income_dict["total_amount"]]
#         total_amount = [income_dict["total_amount"].get(key) for key in income_dict["total_amount"]]
#         deduction_amount = [income_dict["deduction_amount"].get(key) for key in income_dict["deduction_amount"]]
#         take_home_amount = [income_dict["take_home_amount"].get(key) for key in income_dict["take_home_amount"]]
#         agg_result.append(
#             {
#                 "labels": labels,
#                 "total_amount": total_amount,
#                 "deduction_amount": deduction_amount,
#                 "take_home_amount": take_home_amount,
#             }
#         )
#     else:
#         agg_result.append(
#             {
#                 "labels": [],
#                 "total_amount": [],
#                 "deduction_amount": [],
#                 "take_home_amount": [],
#             }
#         )
#
#     return agg_result
#
#
# def valid_income_forecast_request_check(request):
#     """年収推移登録データへの妥当性チェック"""
#
#     result = []
#     req_data = request.data[RequestDateType.ENTRY_DATA.value]
#     for idx in range(0, len(req_data)):
#         for key, val in req_data[idx].items():
#             valid_items = each_items_valid(key, val)
#             result.append(valid_items)
#
#     if len(result) > 0:
#         error_list = ['{0}行目で、{1}項目でのバリデーションエラー'.format(idx + 1, vals)
#                       for idx, val in enumerate(result) for vals in val]
#         return error_list
#
#     return result
#
#
# def update_income_request(queryset, serializer, key_id, id_value, request):
#     """年収推移データ更新、登録"""
#
#     query_request = request.data[RequestDateType.ENTRY_DATA.value]
#     for data in query_request:
#         existing_data = data.get('income_forecast_id', None)
#
#         filter_dict = {
#             key_id: request.data.get(id_value, ""),
#         }
#
#         if existing_data is not None:
#             filter_dict["income_forecast_id"] = existing_data
#
#         result = []
#         query = queryset.objects.filter(**filter_dict).first()
#         query_request = request.data[RequestDateType.ENTRY_DATA.value]
#         for res in query_request:
#             res["update_user"] = str(request.user)
#             res["delete_flag"] = "0"
#             res["user"] = filter_dict[key_id]
#             if query and existing_data:
#                 # user_idが同一の場合は更新処理
#                 serializer = serializer(instance=query, data=res)
#                 if serializer.is_valid(raise_exception=True):
#                     serializer.save()
#                 elif not serializer.save():
#                     result = "更新失敗"
#                 else:
#                     result = "更新内容エラー"
#             else:
#                 # user_idが異なる場合新規登録処理
#                 serializer = serializer(data=res)
#                 if serializer.is_valid(raise_exception=True):
#                     serializer.save()
#                 elif not serializer.save():
#                     result = "DB登録失敗"
#                 else:
#                     result = "DB登録内容エラー"
#
#         return result
#
#
# def update_income_forecast_request(request):
#     """年収表データの登録、更新"""
#     result = valid_income_forecast_request_check(request)
#     if len(result) > 0:
#         return result
#
#     result = update_income_request(IncomeForecastData,
#                                    IncomeForecastDataSerializer,
#                                    IncomeForecastColumnName.USER_ID.value,
#                                    RequestDateType.USER_ID.value,
#                                    request)
#
#     return result