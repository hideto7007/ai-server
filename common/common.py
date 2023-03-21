import datetime
import requests
import re
from django.contrib.sessions.models import Session


def save_session(request):
    if not request.session.session_key:
        request.session.save()
    else:
        if request.session.exists(request.session.session_key) == False:
            request.session.save()


def check_session(request):
    # この関数を呼び出さないとCookiesに反映さえない
    # しかし、save_session関数をここで実装するとCookiesの値を削除しても自動で生成される
    save_session(request)
    if request.session.exists(request.session.session_key) == True:
        return True
    else:
        return False

def check_login(request):
    login = True
    if not check_session(request):
        login = False
    return login

def registrationValueToSession(request, key, value):
    """指定されたキーをセッションに保存する"""

    if check_session(request):
        request.session[key] = value