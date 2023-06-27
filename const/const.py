from enum import IntEnum, Enum


class ApiResultKind(IntEnum):
    """API応答結果"""
    RESULT_SUCCESS = 0
    RESULT_ERROR = 1

class ObjectDetectionModelColumn(Enum):
    """物体検知モデル表示用カラムデータ"""
    ID = "id"
    OBJECT_DETECTION_MODEL_NAME = "object_detection_model_name"
    OBJECT_DETECTION_MODEL_NAME_ID = "object_detection_model_name_id"

class ProjectColumn(Enum):
    """プロジェクト表示用カラムデータ"""
    ID = "id"
    PROJECT_NAME = "project_name"

class AccountColumn(Enum):
    """アカウント表示用カラムデータ"""
    ID = "id"

class RequestDateType(Enum):
    """登録データ"""
    ENTRY_DATA = "data"
    ID = "id"
    USER_ID = "user_id"


class PathList(Enum):
    """登録及び削除パス一覧"""
    path_list = ["./evals/model", "./evals/input", "./evals/output"]
