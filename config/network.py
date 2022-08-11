"""网络错误模型

"""
import enum
from functools import lru_cache


class NetworkState(enum.Enum):
    _ok = "Success"
    _fail = "Fail"


class NetworkSuccess(enum.IntEnum):
    HTTP_SUCCESS = 200
    HTTP_CREATED = 201
    HTTP_ACCEPTD = 202
    HTTP_NONAUTH = 203
    HTTP_NO_CONTENT = 204
    HTTP_RESET_CONTENT = 205
    HTTP_PARTIAL_CONTENT = 206


class NetworkFailure(enum.IntEnum):

    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_FORBIDDEN = 403
    HTTP_NOT_FOUND = 404
    HTTP_METHOD_NOT_ALLOWED = 405
    HTTP_NOT_ACCEPTABLE = 406
    HTTP_PROXY_AUTHENTICATION_REQUIRED = 407
    HTTP_REQUEST_TIMEOUT = 408
    HTTP_REQUEST_CONFLICT = 409
    HTTP_GONE = 410
    HTTP_LENGTH_REQUIRED = 411
    HTTP_PRECONDITION = 412
    HTTP_REQUEST_ENTITY_TOO_LARGE = 413
    HTTP_REQUEST_URL_TOO_LONG = 414
    HTTP_UNSUPPORTED_MEDIA_TYPE = 415
    HTTP_REQUESTED_RANGE_NOT_STATISFIABLE = 416
    HTTP_EXPECTATION = 417
    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_BAD_GATEWAY = 502
    HTTP_SERVICE_UNAVAILABLE = 503
    HTTP_GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505


class HttpState(object):
    Success = NetworkSuccess
    Failure = NetworkFailure
    State = NetworkState
    condition = {
        # // 请求正常部分
        NetworkSuccess.HTTP_SUCCESS: (NetworkState._ok, "请求正常"),
        NetworkSuccess.HTTP_CREATED: (NetworkState._ok, "请求已经创建,正在执行中..."),
        NetworkSuccess.HTTP_ACCEPTD: (NetworkState._ok, "接受请求"),
        NetworkSuccess.HTTP_NONAUTH: (NetworkState._ok, "非官方信息"),
        NetworkSuccess.HTTP_NO_CONTENT: (NetworkState._ok, "无内容"),
        NetworkSuccess.HTTP_RESET_CONTENT: (NetworkState._ok, "重置内容"),
        NetworkSuccess.HTTP_PARTIAL_CONTENT: (NetworkState._ok, "局部内容"),
        # // 请求错误部分
        NetworkFailure.HTTP_BAD_REQUEST: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_UNAUTHORIZED: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_FORBIDDEN: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_NOT_FOUND: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_METHOD_NOT_ALLOWED: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_NOT_ACCEPTABLE: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_PROXY_AUTHENTICATION_REQUIRED: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_REQUEST_TIMEOUT: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_REQUEST_CONFLICT: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_GONE: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_LENGTH_REQUIRED: (NetworkState._fail, "错误请求"),
        NetworkFailure.HTTP_BAD_GATEWAY: (NetworkState._fail, "错误请求"),
    }

    @classmethod
    def match(cls, status):
        _code, _msg = cls.condition[status]
        return _code, {"code": status.value, "msg": _msg}, status.value


if __name__ == "__main__":
    HttpState.match(HttpState.Success.HTTP_ACCEPTD)
    HttpState.match(NetworkFailure.HTTP_BAD_GATEWAY)
    HttpState.match(NetworkFailure.HTTP_GONE)
    HttpState.match(NetworkFailure.HTTP_BAD_GATEWAY)
