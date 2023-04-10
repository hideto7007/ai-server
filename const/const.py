from enum import IntEnum, Enum


class ApiResultKind(IntEnum):
    """API応答結果"""
    RESULT_SUCCESS = 0
    RESULT_ERROR = 1

class ObjectDetectionModelColumn(Enum):
    """物体検知モデル表示用カラムデータ"""
    ID = "id"
    OBJECT_DETECTION_MODEL_NAME = "object_detection_model_name"

class RequestDateType(Enum):
    """登録データ"""
    ENTRY_DATA = "data"
    ID = "id"
    USER_ID = "user_id"