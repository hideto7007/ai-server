import datetime
import requests
import re
from django.contrib.sessions.models import Session
from const.const import RequestDateType


def datetime_str_replace(date, before_format, after_format):
    """datetimeや文字列日付を指定の文字列日付へ置換"""

    before_date = datetime.datetime.strptime(date, before_format)
    after_date = before_date.strftime(after_format)

    return after_date


def blank_check(value):
    """空行であることのチェック"""

    blank = False
    if value is None or (isinstance(value, str)) and 0 == len(value):
        blank = True
    return blank

def int_check(value):
    """整数値チェック"""
    valid = True
    if type(value) == str or type(value) == float or value is None:
        valid = False
        return valid

    if value <= 0:
        valid = False
        return valid

    return valid


def value_check(value):
    """
    　　値チェック
       --------
    　　value_checkの説明
       値があれば真、無ければ偽
    """

    valid = True
    if value is None or len(value) == 0:
        valid = False

    return valid

def uuid_check(value):
    """
        uuidチェック
    ------
        param: str
            文字列のuuid
        return: boolen
    ------
    """

    valid = True
    if value is None or len(value) == 0 or len(value) != 36:
        valid = False

    return valid


def datetime_valid_check(value, required, date_format):
    """
        日付バリデーションチェック
        parameters
        ----------
        value: str
            日付
        required: boolean
           True = 必須/False = 任意
        date_format: str
            str→date型に変換する際の日付フォーマット
        return: boolen
    """

    valid = True
    try:
        if not datetime.datetime.strptime(value, date_format) and required:
            valid = False
    except ValueError:
        valid = False

    return valid


def valid_date(value, required):
    """
       妥当性チェック
    -------
    required: boolean
       True = 必須/False = 任意
    -------
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required or value_check(value):
        valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        valid = True

    return valid


def valid_date_digit_int(value, required, min, max):
    """
       整数一桁からの妥当性チェック
       -------
       required: boolean
          True = 必須/False = 任意
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required or value_check(value):
        if re.match(r"^[0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    return valid


def valid_date_double_digit_int(value, required, min, max):
    """
       整数二桁からの妥当性チェック
       -------
       required: boolean
          True = 必須/False = 任意
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required or value_check(value):
        if re.match(r"^[1-9][0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[1-9][0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    return valid


def valid_float(value, required, min, max):
    """小数点を含むバリデーションチェック"""

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required or value_check(value):
        if re.match(r"^[+]?[0-9]*[.]?[0-9]+$", value) is not None:
            val = float(value)
            if min <= val <= max:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[+]?[0-9]*[.]?[0-9]+$", value) is not None:
            val = float(value)
            if min <= val <= max:
                valid = True

    return valid


def dbvalue_to_str(value):
    """db取得項目を文字列に変換して返す"""

    result = ""
    if value is not None:
        result = str(value)

    return result

def int_replace(value):
    """
        数値変換
    """

    result = ""
    if value is not None and value != '':
        result = int(value)
    return result


def valid_int(value, required):
    """
       整数0以上バリデーションチェック
       -------
       required: boolean
          True = 必須/False = 任意
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required or value_check(value):
        if re.match(r"^[1-9][0-9]*$", value) is not None:
            val = int(value)
            if val >= 0:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[1-9][0-9]*$", value) is not None:
            val = int(value)
            if val >= 0:
                valid = True

    return valid


def each_items_valid(key, value):
    """各項目バリデーションチェック"""

    result = []
    # 全て必須項目
    required = True
    if key == "id":
        if not valid_date(value, required):
            result.append("id")
    elif key == "name":
        if not valid_date(value, required):
            result.append("物体検知モデル名")
    elif key == "first_name":
        if not valid_date(value, required):
            result.append("苗字")
    elif key == "last_name":
        if not valid_date(value, required):
            result.append("名前")
    elif key == "email":
        if not valid_date(value, required):
            result.append("メールアドレス")
    elif key == "username":
        if not valid_date(value, required):
            result.append("ユーザー名")
    elif key == "password":
        if not valid_date(value, required):
            result.append("パスワード")
    elif key == "project_name":
        if not valid_date(value, required):
            result.append("プロジェクト名")
    elif key == "object_detection_model_name_id":
        if not valid_date(value, required):
            result.append("物体検知ID")

    return result


def valid_request_check(request):
    """登録データへの妥当性チェック"""

    result = []

    for key, val in request.data[RequestDateType.ENTRY_DATA.value][0].items():
        valid_items = each_items_valid(key, val)
        result.append(valid_items)

    if len(result) > 0:
        error_list = ['{0}行目で、{1}項目でのバリデーションエラー'.format(idx + 1, vals)
                      for idx, val in enumerate(result) for vals in val]
        return error_list

    return result


# この関数は使わない
def save_session(request):
    request.session.save()
    # s = Session.objects.get(pk=request.session.session_key)
    # TBD:ここでデータを受け取って存在チェックするように修正する
    # print("確認", s)
    # if not request.session.session_key:
    #     request.session.save()
    # else:
    #     if request.session.exists(request.session.session_key) == False:
    #         request.session.save()
    #         print("request.session.save()", request.session.save())


def check_session(username, token, user_id=None):
    # session存在チェック
    from user.login import get_user_id

    check = True

    # 日付文字列を修正する
    datetime_str_re = lambda target, date_str: date_str[:date_str.find(target)]

    get_datetime = datetime_str_re(".", get_user_id(username, user_id)["last_login"]).replace("T", " ")

    time_diff = datetime.datetime.now() - datetime.datetime.strptime(get_datetime, '%Y-%m-%d %H:%M:%S')

    # 設定時間：1時間
    setting_td = datetime.timedelta(hours=1)

    print(time_diff)

    # 規定時間以上ログインしていたらログアウトにする
    if time_diff >= setting_td:
        print("削除")
        delete_request(Session,
                       "session_key",
                       token,
                       True)
        check = False
    else:
        print("ログイン中")
    return check


def check_login(username, token, user_id):
    login = True
    if not check_session(username, token, user_id):
        login = False
    return login


def registrationValueToSession(request, key, value, user_id):
    """指定されたキーをセッションに保存する"""

    if check_session(request, value, user_id):
        request.session[key] = value


def delete_request(queryset, param_id, str_id, session_flag=False):
    """登録データ削除"""

    if not value_check(str_id):
        result = "idが不正です"
        return result

    # 削除対象のid取得する
    # sessionにはdelete_flagがない為、分岐させて取得パラメータのみにする
    if session_flag:
        filter_dict = {param_id: str_id}
    else:
        filter_dict = {"delete_flag": 0, param_id: str_id}

    queryset_delete_request = queryset.objects.filter(**filter_dict)
    # DB登録データ削除
    queryset_delete_request.delete()
    result = []
    if not queryset_delete_request.delete():
        result = "DB登録データ削除失敗"

    return result


def get_best_new_id(queryset, serializer):
    """最も新しいidを取得"""

    return int(serializer(queryset.objects.order_by('-id'), many=True).data[0]['id'])