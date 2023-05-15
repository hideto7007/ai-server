from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from common.common import check_login, delete_request
from .coomon import (
    update_account_request,
    get_user_info,
    update_password
)
from const.const import ApiResultKind
from django.contrib.auth.models import User
from .serializers import UserSerializer

class CreateUpdateAccountAPIView(views.APIView):
    """アカウント登録・更新APIクラス"""

    def post(self, request, *args, **kwargs):

        result_code = ApiResultKind.RESULT_SUCCESS
        detail = {}

        if check_login(request):
            # バリデート一つでもエラーがあれば中断
            result_array = update_account_request(request)

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


class UserInfoListAPIView(views.APIView):
    """アカウント取得APIクラス"""

    def get(self, request, *args, **kwargs):

        if check_login(request):
            result = get_user_info(request.GET.get("id"))

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


class PasswordUpdateAPIView(views.APIView):
    """パスワード更新APIクラス"""

    def post(self, request, *args, **kwargs):

        result_code = ApiResultKind.RESULT_SUCCESS
        detail = {}

        if check_login(request):
            # バリデート一つでもエラーがあれば中断
            result_array = update_password(request)

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