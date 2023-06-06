from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from common.common import check_login, delete_request
from project.common import (
    get_project_model_list,
    update_project_request
)
from const.const import ApiResultKind, ProjectColumn
from project.models import Project


class ProjectlListAPIView(views.APIView):
    """プロジェクトデータ取得APIクラス"""

    def get(self, request, *args, **kwargs):

        if check_login(request.GET.get("username"), request.GET.get("token"), request.GET.get("user_id")):
            result = get_project_model_list(request.GET.get("model_name"), request.GET.get("id"))

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



class ProjectDeleteAPIView(views.APIView):
    """プロジェクトデータ削除APIクラス"""

    def post(self, request, *args, **kwargs):
        """物体検知モデルデータ削除"""

        if check_login(request.data["params"][0]["username"],
                       request.data["params"][0]["token"],
                       request.data["params"][0]["user_id"]):
            result_code = ApiResultKind.RESULT_SUCCESS
            result_array = delete_request(Project,
                                          ProjectColumn.ID.value,
                                          request.data[ProjectColumn.ID.value])

            if len(result_array) == 0:
                result_code = result_code
                message = "Success"
            else:
                result_code = ApiResultKind.RESULT_ERROR
                message = "DB登録データ削除エラー"

            return JsonResponse(
                {"result_code": result_code,
                 "message": message}, safe=False
            )
        else:
            request = {"result_code": 1, "message": "セッションの有効期限が切れています。"}

            return JsonResponse(request, safe=False)


class ProjectPostListAPIView(views.APIView):
    """プロジェクトデータ登録・更新APIクラス"""

    def post(self, request, *args, **kwargs):

        result_code = ApiResultKind.RESULT_SUCCESS
        detail = {}

        if check_login(request.data["params"][0]["username"],
                       request.data["params"][0]["token"],
                       request.data["params"][0]["user_id"]):
            # バリデート一つでもエラーがあれば中断
            result_array = update_project_request(request)

            if len(result_array) == 0:
                result_code = result_code
                message = "Success"
            else:
                result_code = ApiResultKind.RESULT_ERROR
                message = "登録及び更新エラー"
                detail["error_list"] = result_array

            return JsonResponse(
                {"result_code": result_code, "message": message, "detail": detail}, safe=False
            )
        else:
            request = {"result_code": 1, "message": "セッションの有効期限が切れています。"}

            return JsonResponse(request, safe=False)
