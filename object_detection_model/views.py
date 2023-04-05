from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from common.common import check_login
from object_detection_model.common import (get_object_detection_model_list)
from const.const import ApiResultKind


class ObjectDetectionModelListAPIView(views.APIView):
    """物体検知モデルデータ取得APIクラス"""

    def get(self, request, *args, **kwargs):

        if check_login(request):
            # request.GET.get("model_id")
            result = get_object_detection_model_list()

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
