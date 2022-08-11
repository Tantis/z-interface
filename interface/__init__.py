

from .main import *                 # 加载FLASK配置以及其他功能
from .resource import *             # 加载FLASK基础接口功能
from orm.model import *             # 加载ORM模型
from .logger import logger          # 加载日志模块
from utils.event import *           # 加载事件侦听
import atexit


__all__ = ["app", "logger", "db"]


@api.errorhandler
def specific_namespace_error_handler(error):
    '''API ERROR CODE'''
    return {'message': str(error)}, getattr(error, 'code', 500)


@atexit.register
def on_exit():
    """当程序结束时，我们要执行一些必要链接断开行为

    """
    logger.info("[on_exit] 开始进行清理...")
