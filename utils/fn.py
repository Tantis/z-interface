import time
import traceback
from functools import wraps
from interface.logger import logger
from .ob import model
from config.network import HttpState


def Timefn(f):
    # 计算方法运行时间

    @wraps(f)
    def decotor(tm=None):
        currentTime = tm
        startTime = time.time()
        t = f()
        endTime = time.time()
        longTime = startTime - endTime
        print("【执行函数】%s 花费时间: %s" % (f.__name__, longTime))
        return t
    return decotor


def trace_lines(frame, event, arg):
    if event != "line":
        return
    co = frame.f_code
    func_name = co.co_name
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    logger.debug("\n"
                 "[call   to] %s \n"
                 "[on   line] %s of %s \n"
                 "[from line] %s of %s \n"
                 % (func_name, func_line_no, func_filename, caller_line_no, caller_filename))


def trace_calls(frame, event, arg):
    if event != "call":
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name in ["get", "post", "put", "delete", "LoginResource"]:
        return trace_lines
    return


def befor(befor_func, s=HttpState):
    print(befor_func.__name__, s.__name__)

    def wapper(f):

        _real_name = f.__name__ + '[befor request]'
        logger.info(_real_name)

        @wraps(f)
        def __console(*ar, **kw):
            logger.debug(str(ar), str(kw))
            try:
                state, response, code = befor_func()
                if state == s.State._fail:
                    logger.info("[%s] request fail code: %s" %
                                (_real_name, code))
                    return state, response, code
            except Exception as err:
                traceback.print_exc()
                state, bad_req, code = s.match(s.Failure.HTTP_BAD_REQUEST)
                return state, bad_req, code
            kw["args"] = model(response)
            result = f(*ar, **kw)
            return result
        return __console
    return wapper


def after(target, s=HttpState):
    """ 函数执行之后是否执行某函数

    """
    def control(func, *args, **kwarg):
        _real_name = func.__name__ + '[befor request]'

        @wraps(func)
        def __console(*ag, **kw):
            try:
                state, response, code = func(*ag, **kw)
                if state == s.State._fail:
                    logger.info("[%s] request fail code: %s" %
                                (_real_name, code))
                    return state, response, code
                kw["response"] = response
                state, result, code = target(**kw)
                return state, result, code
            except Exception as err:
                traceback.print_exc()
                _, bad_req, code = s.match(s.Failure.HTTP_BAD_REQUEST)
                return state, bad_req, code
        return __console
    return control


def last(response_func):
    def decotor(f):
        def wapper(*ag, **kw):
            _, response, code = f(*ag, **kw)
            return response_func(response, code)
        return wapper
    return decotor
