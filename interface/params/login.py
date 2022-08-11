"""验证参数类

"""
from flask import request
from config.network import HttpState


class Args:

    @staticmethod
    def login():

        _args = request.args
        _json = request.json or dict()
        _from = request.data
        _header = request.headers
        payloads = {
            "args": dict(_args),
            "json": dict(_json),
            "from": dict(_from),
            "header": dict(_header),
        }
        return HttpState.State._ok, payloads, HttpState.Success.HTTP_SUCCESS
