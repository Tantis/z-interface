from flask_restplus import fields
from werkzeug.datastructures import FileStorage
from .bases import DocumentFormat


"""data类示例

"""


class _params:

    dt = DocumentFormat

    def header(self, api):
        _tk = self.dt(_name="header_token", _type=str,
                      _required=True, _location="header",
                      _value="", _description="在头部添加Token信息")
        _ac = self.dt(_name="header_access_token", _type=str,
                      _required=True, _location="header",
                      _value="", _description="在头部添加接入信息")
        _hader_result = self.dt(_value=[_tk, _ac],
                                parse=api.parser()).params()
        return api.doc(parser=_hader_result)

    def login(self, api):
        token = self.dt(_name="token", _type=str,
                        _required=True, _location="query",
                        _value="", _description="登录后的token信息")
        access_token = self.dt(_name="access_token", _type=str,
                               _required=True, _location="query",
                               _value="", _description="接入的token信息")
        _login_result = self.dt(_value=[token, access_token],
                                parse=api.parser()).params()
        return api.doc(parser=_login_result)


class _body:

    dt = DocumentFormat

    def login(self, api):
        _account = self.dt(_type=str, _value="user01",
                           _description="账户", _value_ext=dict(
                               min_length=7, max_length=15
                           ))
        _password = self.dt(_type=str, _value="user01",
                            _description="密码", _value_ext=dict(
                                min_length=7, max_length=15
                            ))
        _renew = self.dt(
            _type=dict,
            _value={
                "account": _account,
                "password": _password
            },
            _name="user_account_number_01",
        )
        return api.doc(body=_renew.json(api))


params = _params()
body = _body()
