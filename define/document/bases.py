from dataclasses import dataclass, field
from typing import Any
# from interface import api
# from flask_restplus import Api
from flask_restplus import reqparse
from flask_restplus import Model, fields


@dataclass
class DocumentFormat:
    """ 文档 初始类 """

    _value: Any
    _type: Any = str
    _name: Any = ""
    _description: Any = ""
    _required: Any = False
    _location: Any = "query"
    _value_ext: dict = field(default_factory=dict)
    parse: Any = reqparse.RequestParser()
    __swich_fields_keys = {
        "str": fields.String,
        "int": fields.Integer,
        "float": fields.Float,
        "Decimal": fields.Arbitrary,
        "unicode": fields.String,
    }
    api: Any = Model

    def params(self):
        parse = self.parse.copy()
        if isinstance(self._value, (list, tuple)):
            for _parase in self._value:
                parse.add_argument(_parase._name, type=_parase._type, required=self._required,
                                   help=_parase._description, default=_parase._value, location=_parase._location)
        return parse

    def _nested_item(self, key, val):
        # _fields = fields.Nested(model=Model(
        #     key,
        #     self._json(key, val),
        #     description=u'字典数据'))
        print("next _json")
        return self._json(key, val)

    def _nested_list(self, key, val):
        _all_fileds = []
        for _val in val._value:
            if isinstance(_val._value, dict):
                _fileds = self._nested_item(key, val._value)
            elif isinstance(_val._value, list):
                _fileds = self._list(key, _val)
            else:
                _type = self._type_check(_val)
                _fileds = _type(
                    _val._value, description=_val._description, **self._value_ext)
            _all_fileds.append(_fileds)
        return _all_fileds

    def _type_check(self, _rtype):
        try:
            _type = self.__swich_fields_keys.get(str(_rtype._type.__name__))

            if not _type:
                return _rtype
            return _type
        except Exception as er:
            print(_rtype)
            raise TypeError(11)

    def _nested_dict(self, value):

        _repq = value
        _models = {}
        for _k, _v in _repq.items():
            if isinstance(_v._value, dict):
                _fields = self._nested_item(_k, _v)
            elif isinstance(_v._value, list):
                # _fields = self._nested_list(_v._name, _v)
                _fields = self._list(_v._name, _v)
            else:
                _type = self._type_check(_v)
                _fields = _type(
                    _v._value, description=_v._description, **self._value_ext)
            _models[_k] = _fields
        print(_models)

        return _models

    def _json(self, name, value):
        _result = self._nested_dict(value._value)
        model = Model(value._name, _result)
        if self.api:
            model = self.api.model(value._name, _result)
        return fields.Nested(model=model)

    def _list(self, name, value):
        model = self._nested_list(name, value)

        _result = fields.List(
            model[0]
        )

        return _result

    def json(self, api=None):
        self.api = api
        result = Model(self._name)
        if isinstance(self._value, (dict)):
            models = self._nested_dict(self._value)
            result = fields.Nested(model=Model(
                models), description=self._description)
        elif isinstance(self._value, list):
            result = fields.List(
                self._name,
                model=self._nested_list(self._name, self._value))

        print(result)
        if api:
            api.models[self._name] = result
            return api.model(self._name, models)
        return result

    def response(self):

        return

    def extends(self, doc):

        return


if __name__ == "__main__":
    new = DocumentFormat(_type=int, _value=1, _description="这是一个测试数据")

    _renew = DocumentFormat(
        _type=list,
        _value={
            "list": DocumentFormat(_value=[
                DocumentFormat(_type=str, _value="user01",
                               _description="这是一个测试数据"),
                new
            ], _name="LG_body_req"),
            "code": DocumentFormat(_type=int, _value=200, _description="这是一个测试数据")
        },
        _description="这是一个测试数据")
    par = _renew.json()
    print(par)
    import ipdb
    ipdb.set_trace()

    print(new)
    print(isinstance(new, DocumentFormat))
