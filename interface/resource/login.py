#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
import random


from define import *
from interface.main import api, db
from interface.logger import logger
from orm.model import User
from flask import request
from flask_restplus import Resource
from define.document import params, body
from utils.fn import befor
from interface.params.login import Args
from config.network import HttpState


class LoginResource(Resource):
    num = 1

    @params.login(api)
    @befor(Args.login, HttpState)
    def get(self, args):
        """获取登录信息

        """
        state, response, code = HttpState.match(HttpState.Success.HTTP_SUCCESS)
        response["data"] = args
        return response, code

    # @DocFormat.response(name="responseLogin", data=defaultResponse)
    # @DocFormat.model(data=defaultJson, name="postLogin")
    # @api.doc(parser=_relast.params())
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
