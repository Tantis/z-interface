#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2019
# All rights reserved

from flask_restplus import Model, fields
from datetime import datetime, date, timedelta
import time
from flask_restplus.fields import string_types, datetime_from_iso8601, datetime_from_rfc822
import copy


def new_marshal(sourceData, updateData):
    assert isinstance(sourceData, dict)
    assert isinstance(updateData, dict)
    newData = sourceData.copy()
    newData.update(updateData)
    return newData


def fields_getAttrValue(key, default=None):
    def _getValue_(data):
        if isinstance(data, dict):
            value = data.get(key, default)
        else:
            value = setattr(data, key, default)
        return value

    return _getValue_


class Fields_DataTime(fields.DateTime):

    def __init__(self, *args, **kwargs):
        dt_format = kwargs.get('dt_format', 'iso8601')
        if dt_format == 'normal':
            self.__schema_example__ = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif dt_format == 'duration':
            self.__schema_example__ = '00:08:08'
        super(Fields_DataTime, self).__init__(*args, **kwargs)

    def parse(self, value):
        if value is None:
            return None
        elif isinstance(value, string_types):
            parser = datetime_from_iso8601 if self.dt_format == 'iso8601' else datetime_from_rfc822
            return parser(value)
        elif isinstance(value, datetime):
            return value
        elif isinstance(value, date):
            return datetime(value.year, value.month, value.day)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError('Unsupported DateTime format')

    def format_normal(self, dt):
        '''
        Turn a datetime object into a formatted date.

        :param datetime dt: The datetime to transform
        :return: A RFC 822 formatted date string
        '''
        if isinstance(dt, datetime):
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(dt, int):
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(dt))
        return dt

    def format_duration(self, dt):
        return str(timedelta(seconds=dt))

    def format(self, value):
        try:
            value = self.parse(value)
            if self.dt_format == 'iso8601':
                return self.format_iso8601(value)
            elif self.dt_format == 'rfc822':
                return self.format_rfc822(value)
            elif self.dt_format == 'normal':
                return self.format_normal(value)
            elif self.dt_format == 'duration':
                return self.format_duration(value)
            else:
                raise fields.MarshallingError(
                    'Unsupported date format %s' % self.dt_format
                )
        except (AttributeError, ValueError) as e:
            raise fields.MarshallingError(e)


default200_Model = Model('default_200_Model', {
    'msg': fields.String(default=''),
    'resultCode': fields.Integer(default=0),
    'status': fields.Integer(default=200),
    'errStatus': fields.Integer(default=200, example=200),
})

default200_Data_Model = Model('default_200_Data_Model', {
    'msg': fields.String(default='', example='成功'),
    'resultCode': fields.Integer(default=200, example=200),
    'status': fields.Integer(default=200, example=200),
    'errStatus': fields.Integer(default=200, example=200),
    'data': fields.Raw,
})

default400_Model = Model('default_400_Model', {
    'errors': fields.Raw,
    'msg': fields.String(default='', example='失败'),
    'resultCode': fields.Integer(default=400, example=400),
    'status': fields.Integer(default=400, example=400),
    'errStatus': fields.Integer(default=400, example=400),
})
default403_Model = Model('default_403_Model', {
    'msg': fields.String(default='', example='失败'),
    'resultCode': fields.Integer(default=403, example=403),
    'status': fields.Integer(default=403, example=403),
    'errStatus': fields.Integer(default=403, example=403),
})

default404_Model = Model('default_404_Model', {
    'msg': fields.String(default='', example='失败'),
    'resultCode': fields.Integer(default=404, example=404),
    'status': fields.Integer(default=404, example=404),
    'errStatus': fields.Integer(default=404, example=404),
})

User_Simaple_Model = Model('user_detailed_simple', {
    'uid': fields.Integer(attribute='id'),
    'nickname': fields.String,
    'avatar_url': fields.String,
})

User_Simaple_Model_List_Data = Model('footprint_detailed_list', {
    "list": fields.List(fields.Nested(User_Simaple_Model)),
    'next': fields.Boolean(default=False),
})

User_Simaple_Model_List = Model.clone('user_detailed_simple_list', default200_Data_Model, {
    'data': fields.Nested(User_Simaple_Model_List_Data)

})

default_marshal = {
    200: {'description': '成功', 'fields': default200_Model, 'skip_none': True},
    404: {'description': '操作失败', 'fields': default404_Model},
    403: {'description': '10403:TOKEN不存在;10401:ACCESS_TOKEN不存在', 'fields': default403_Model},
    400: {'description': '传入的参数不合法', 'fields': default400_Model},
}

defaultData_marshal = {
    200: {'description': '成功', 'fields': default200_Data_Model, 'skip_none': True},
    404: {'description': '操作失败', 'fields': default404_Model},
    403: {'description': '10403:TOKEN不存在;10401:ACCESS_TOKEN不存在', 'fields': default403_Model},
    400: {'description': '传入的参数不合法', 'fields': default400_Model},
}


def getNew_marshal(updateFields, sourceMarshal=default_marshal, status=200):
    assert isinstance(sourceMarshal, dict)
    assert isinstance(updateFields, Model)
    newMarshal = copy.deepcopy(sourceMarshal)
    newMarshal[status]['fields'] = updateFields
    return newMarshal


deafultData_UserList_Simple_marshal = getNew_marshal(
    updateFields=User_Simaple_Model_List)
