import datetime
import requests
import re
from django.contrib.sessions.models import Session


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