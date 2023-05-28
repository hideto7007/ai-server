from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError, JsonResponse, \
    HttpResponseNotFound
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from rest_framework.views import APIView
from rest_framework import generics, viewsets, views
import logging

import json

from common.common import check_login, check_session, registrationValueToSession


# views.APIView
# View
class Login(views.APIView):
    """ログインAPI"""

    @csrf_exempt  # csrf無効化
    def dispatch(self, *args, **kwargs):
        return super(Login, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        response = {}
        params = json.loads(request.body.decode())

        # username及びpasswordがないとき、又は空欄のときはエラー
        if params.get("username", "") == "" or params.get("password", "") == "":
            logging.info(params.get("username", "") + "login username failed")
            logging.info(params.get("password", "") + "login password failed")
            response = {"result": 1, "message": "ID又はpsを入力して下さい"}
            return HttpResponseBadRequest(json.dumps(response))

        # django_user_authから認証する
        user_auth = authenticate(request, username=params.get("username"), password=params.get("password"))

        # Noneであれば認証失敗
        if user_auth is None:
            logging.info(params.get("username", "") + "login username failed")
            response = {"result": 1, "message": "ID又はpsを入力して下さい"}
            return HttpResponseBadRequest(json.dumps(response))

        else:
            username = vars(user_auth).get("username")

            # djangoにログインしたことを伝える
            login(request, user_auth)

            get_id = get_user_id(username, None)

            # セッション作成
            check_session(username, request.session.session_key)

            # セッションに格納
            # registrationValueToSession(request, "username", username, get_id.get("id"))

            # レスポンス生成
            response = {
                "result": 0,
                "message": "success",
                "detail": {
                    "username": params.get("username"),
                    "params_id": get_id.get("id"),
                    "token": request.session.session_key
                }
            }
            logging.info(params.get("username") + "logged in")

        return JsonResponse(response, safe=False)


def get_user_id(username_str, user_id):
    """userのid取得"""

    if user_id is None:
        user_list = User.objects.filter(username=username_str)
    else:
        user_list = User.objects.filter(username=username_str, id=user_id)
    result = []
    for res in UserSerializer(user_list, many=True).data:
        result.append(
            {
                "id": res["id"],
                "username": res["username"],
                "last_login": res["last_login"]
            }
        )

    return result[0]
