import time
from functools import wraps
from interface.logger import logger


# 计算方法运行时间
def Timefn(f):

    @wraps(f)
    def decotor():
        startTime = time.time()
        t = f()
        endTime = time.time()
        longTime = startTime - endTime
        logger.info("【执行函数】%s 花费时间: %s" % (f.__name__, longTime))
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
