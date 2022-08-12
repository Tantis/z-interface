#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
import random
from define import *

from interface.logger import logger
from interface.main import api, db
from interface.params.login import Args
from interface.process.login import LoginProcess
from interface.response import DefualtResponse
from config.network import HttpState

from orm.model import User
from flask_restplus import Resource
from define.document import params, body
from utils.fn import befor, after, last


@params.header(api)
class LoginResource(Resource):

    @params.login(api)                   # 装在文档
    @last(DefualtResponse.cors_response)               # 最后返回
    @after(LoginProcess.continue_login)  # 逻辑操作
    @after(LoginProcess.first_login)     # 逻辑操作
    @befor(Args.login)                   # 参数验证
    def get(self, args):
        """获取登录信息

        """
        _ok, response, code = HttpState.match(HttpState.Success.HTTP_SUCCESS)
        response["data"] = args
        return _ok, response, code

    @body.login(api)
    def post(self, args):
        """ 登陆 

        """
        maxId = User.query.filter(User.id > 0).order_by(User.id).first()
        logger.info("%s" % maxId)
        tom = User(id=random.randint(1, 1000000), name="test")
        try:
            db.session.add(tom)
            db.session.commit()
        except Exception as e:
            logger.error("提交出错", e)
        finally:
            result = User.query.all()
        jsonp = {i.id: i.name for i in result}
        return jsonp


ns = api.namespace('login', description="用户登陆")
ns.add_resource(LoginResource, "")
