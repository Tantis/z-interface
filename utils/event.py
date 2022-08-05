"""监听Flask事件

"""
from interface import logger
from flask import signals


@signals.request_started.connect
def request_started(*args, response={}, **kwargs):
    """信号请求到来前执行函数
    
    """
    logger.info("[请求] %s-%s-%s" % (args,response, kwargs))
    return response

@signals.request_finished.connect
def request_finished(*args,response={}, **kwargs):
    """信号请求后执行函数
    
    """
    logger.info("[返回] %s-%s-%s" % (args,response, kwargs))
    return response