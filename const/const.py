from enum import IntEnum, Enum


class ApiResultKind(IntEnum):
    """API応答結果"""
    RESULT_SUCCESS = 0
    RESULT_ERROR = 1
