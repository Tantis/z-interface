
from flask import make_response


class DefualtResponse:

    @staticmethod
    def cors_response(response, code):

        rsp = make_response(response, code)
        return rsp
