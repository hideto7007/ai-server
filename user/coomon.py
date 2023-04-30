from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from const.const import RequestDateType, AccountColumn
from common.common import valid_request_check, valid_request_check


def get_best_new_id():
    """最も新しいidを取得"""

    return int(UserSerializer(User.objects.order_by('-id'), many=True).data[0]['id'])


def update_request(queryset, serializer, key_id, id_value, request):

    """データ更新、登録"""

    # 一番最新のidに対してプラス1して、id取得する
    id_value = str(get_best_new_id() + 1)

    filter_dict = {
        key_id: id_value
    }

    result = []
    save_query = queryset.objects.filter(**filter_dict).first()
    query_request = request.data[RequestDateType.ENTRY_DATA.value]

    for res in query_request:
        res["id"] = id_value
        res["is_active"] = True
        res["is_superuser"] = True
        res["is_staff"] = True
        res["password"] = make_password(res["password"])

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


def update_account_request(request):
    """アカウントの登録、更新"""
    result = valid_request_check(request)
    if len(result) > 0:
        return result

    result = update_request(User,
                            UserSerializer,
                            AccountColumn.ID.value,
                            request.data["data"][0][RequestDateType.ID.value],
                            request)

    return result