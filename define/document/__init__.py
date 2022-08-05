#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2016 yu.liu <showmove@qq.com>
# All rights reserved

"""文档驱动模块

"""

import json
import uuid
from flask_restplus import fields
from interface import api
from flask_restplus.utils import merge
import uuid
# from .document import *


class NotDocumentError(Exception):
    pass


class DocFormat:
    __swich_fields_keys = {
        "str": fields.String,
        "int": fields.Integer,
        "float": fields.Float,
        "Decimal": fields.Arbitrary,
        "unicode": fields.String,
    }

    @classmethod
    def NestedList(self, data):
        """返回列表中的数据

        """
        _fileds = {}
        for _key in data:
            if isinstance(_key, dict):
                _fileds = self.NestedDict(_key)
            if isinstance(_key, list):
                _fileds = self.NestedList(_key)
            if isinstance(_key, tuple):
                pass
                # types = _key[0]
                # output = _key[1]
                # description = _key[2]
                # #_fileds = output
                # _fileds = types(
                #     output, description=description,
                # )
        return _fileds

    @classmethod
    def NestedDict(self, data, name=''):
        """返回字典里面的数据

        """
        return self.ResponseBody(data, name, response_fileds=True)

    @classmethod
    def ResponseBody(self, data, model_name, response_model="model", response_code="200", response_data="成功",
                     response_templates=None, response_fileds=False, function=None):
        """返回整个BODY
        :params data          : response data
        :params response_model: model | response
        :return : response data model
        """
        if not model_name:
            model_name = str(uuid.uuid4()).replace('-', '')

        models = {}
        for _key in data:
            if isinstance(data[_key], dict):
                _fields = fields.Nested(model=api.model(
                    model_name+_key,
                    self.NestedDict(
                        data[_key]),
                    description=u'字典数据'))
            elif isinstance(data[_key], list):
                _fields = fields.List(
                    fields.Nested(
                        model=api.model(model_name+_key,
                                        self.NestedList(
                                            data[_key]
                                        ),
                                        description=u'列表数据'
                                        )
                    )
                )
            elif isinstance(data[_key], tuple):
                resultData = data[_key]
                types = resultData[0]
                output = resultData[1]
                description = resultData[2]
                _fields = types(
                    output, description=description
                )
            else:
                resultData = data[_key]
                description = data[_key]
                if type(data[_key]) in [str]:
                    res = data[_key].split(",")
                    if len(res) >= 2:
                        resultData = res[0]
                        description = res[1].strip()
                        _fields = self.__swich_fields_keys[
                            resultData.__class__.__name__](
                            resultData, description=description)
                    else:
                        _fields = self.__swich_fields_keys[
                            data[_key].__class__.__name__](
                            resultData, description=description)
                else:
                    _fields = self.__swich_fields_keys[
                        data[_key].__class__.__name__](
                        resultData, description=description)
            models[_key] = _fields
        if response_fileds:
            return models

        if response_model == "response":
            return api.response(
                response_code, response_data,
                model=api.model(
                    model_name, models))
        return api.doc(body=api.model(model_name, models))

    @classmethod
    def response(self, code="200", response_data="成功", name=None, data={}):
        if not name:
            name = str(uuid.uuid1()).replace("-", '')
        return self.ResponseBody(data, name, response_model="response", response_data=response_data, response_code=code)

    @classmethod
    def model(self, code=0, name=None, data={}, **kwarg):
        if not name:
            name = str(uuid.uuid1()).replace("-", '')
        _result = self.ResponseBody(data, name, response_model="model")
        return _result

    @classmethod
    def paramsBody(cls, data):
        parser = api.parser()
        for _ty in data:
            _type, default, helper, required, location = data[_ty]
            parser.add_argument(_ty, type=_type, required=required,
                                help=helper, default=default, location=location)
        return parser

    @classmethod
    def params(self, name=None, data={}, **kwarg):

        return api.doc(parser=self.paramsBody(data))


Token = api.header("token", description=u"TOKEN")
