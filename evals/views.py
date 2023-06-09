from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import LearningImage

from common.common import check_login, delete_request
from evals.common import (
    EventObject,
    EventHandler
)
from const.const import ApiResultKind, ObjectDetectionModelColumn
from object_detection_model.models import ObjectDetectionModel


class LearningModelDownloadAPIView(views.APIView):
    """学習済みモデルダウンロードAPIクラス"""

    def get(self, request, *args, **kwargs):

        result = []

        if check_login(request.GET.get("username"), request.GET.get("token"), request.GET.get("user_id")):
            # イベントハンドラーオブジェクトを作成
            handler = EventHandler(request.GET.get("object_detection_model_name"),
                                   request.GET.get("project_name"))

            # イベントを処理するオブジェクトを作成
            event_object = EventObject(handler)

            # イベントをトリガー
            result.append(event_object.get_pth_file_trigger_event())
            result.append(event_object.get_input_image_file_trigger_event())
            result.append(event_object.get_output_image_file_trigger_event())

            if isinstance(result, list):
                detail_dic = {"result": result}
                result_code = ApiResultKind.RESULT_SUCCESS
                message = "Success"
            else:
                detail_dic = {}
                result_code = ApiResultKind.RESULT_ERROR
                message = result

            request = {"result_code": result_code, "message": message, "detail": detail_dic}

            return JsonResponse(request, safe=False)
        else:
            request = {"result_code": 1, "message": "セッションの有効期限が切れています。"}

            return JsonResponse(request, safe=False)



# class ObjectDetectionModelDeleteAPIView(views.APIView):
#     """物体検知モデルデータ削除APIクラス"""
#
#     def post(self, request, *args, **kwargs):
#         """物体検知モデルデータ削除"""
#
#         if check_login(request.data["params"][0]["username"],
#                        request.data["params"][0]["token"],
#                        request.data["params"][0]["user_id"]):
#             result_code = ApiResultKind.RESULT_SUCCESS
#             result_array = delete_request(ObjectDetectionModel,
#                                           ObjectDetectionModelColumn.ID.value,
#                                           request.data[ObjectDetectionModelColumn.ID.value])
#
#             if len(result_array) == 0:
#                 result_code = result_code
#                 message = "Success"
#             else:
#                 result_code = ApiResultKind.RESULT_ERROR
#                 message = "DB登録データ削除エラー"
#
#             return JsonResponse(
#                 {"result_code": result_code,
#                  "message": message}, safe=False
#             )
#         else:
#             request = {"result_code": 1, "message": "セッションの有効期限が切れています。"}
#
#             return JsonResponse(request, safe=False)
#
#
# class ObjectDetectionModelPostListAPIView(views.APIView):
#     """物体検知モデル名データ登録・更新APIクラス"""
#
#     def post(self, request, *args, **kwargs):
#
#         result_code = ApiResultKind.RESULT_SUCCESS
#         detail = {}
#
#         if check_login(request.data["params"][0]["username"],
#                        request.data["params"][0]["token"],
#                        request.data["params"][0]["user_id"]):
#             # バリデート一つでもエラーがあれば中断
#             result_array = update_object_detection_model_name_request(request)
#
#             if len(result_array) == 0:
#                 result_code = result_code
#                 message = "Success"
#             else:
#                 result_code = ApiResultKind.RESULT_ERROR
#                 message = "登録及び更新エラー"
#                 detail["error_list"] = result_array
#
#             return JsonResponse(
#                 {"result_code": result_code, "message": message, "detail": detail}, safe=False
#             )
#         else:
#             request = {"result_code": 1, "message": "セッションの有効期限が切れています。"}
#
#             return JsonResponse(request, safe=False)