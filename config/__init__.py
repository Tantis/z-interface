"""各类配置

"""
from distutils.debug import DEBUG
import os
import sys
import enum


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


class Environment(enum.Enum):
    # 环境
    DEVELOPMENT = 0     # 开发
    TESTING = 1         # 测试
    ONLINE = 2          # 生产


class BaseConfigure(object):
    Environment = Environment.DEVELOPMENT

    @classmethod
    def toJson(cls):
        _k = cls.__dict__
        result = dict(filter(lambda x: not x[0].startswith('__'), _k.items()))
        return result

    @classmethod
    def env(cls):
        return cls.Environment


class CeleryConfig(BaseConfigure):
    timezone = 'UTC'
    BROKER_URL = 'redis://localhost:6379/12'            # 消息队列存放地址
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/12'  # celery worker 执行结果返回存放地址
    CELERY_TIMEZONE = 'Asia/Shanghai'                   # 时区

    # 只有当worker执行完任务后，才会告诉MQ，消息被消费。
    CELERY_ACKS_LATE = True
    CELERYD_FORCE_EXECV = True                          # 非常重要,有些情况下可以防止死锁
    CELERY_IGNORE_RESULT = True                         # 忽略结果，不关心运行结果时可以关闭
    CELERY_TASK_SERIALIZER = 'json'                     # 任务序列化方式
    CELERY_DISABLE_RATE_LIMITS = True                   # 对任务消费的速率进行限制开关
    CELERYD_PREFETCH_MULTIPLIER = 1                     # worker预先获取任务数量

    # worker最大执行任务数，超过数量销毁，防止内存泄漏等问题
    CELERYD_MAX_TASKS_PER_CHILD = 30
    CELERY_CREATE_MISSING_QUEUES = True                 # 队列不存在即创建
    BROKER_TRANSPORT_OPTIONS = {
        'visibility_timeout': 7 *
        24 * 60 * 60, 'max_retries': 1}                 # celery worker超时自动重启时间
    CELERYD_CONCURRENCY = 3                             # celery worker 最大并行数


class APP_SETTINGS(BaseConfigure):

    SWAGGER_UI_DOC_EXPANSION = 'list'                   # 文档显示方式
    SQLALCHEMY_TRACK_MODIFICATIONS = True               # 去除SQLALCHEMY 警告内容

    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (        # 默认使用的数据库类型
        os.path.join(PROJECT_ROOT, "example.db"))


class API_SETTING(BaseConfigure):
    doc = False
    version = '1.10.18'
    title = '某API接口管理程序'
    description = '用于展示接口'
    validate = None
    default = '某API 接口'
    default_label = 'Flask API 接口使用案例'
    tags = None
    prefix = ''
    ordered = False
    default_mediatype = 'application/json'
    decorators = None

    if BaseConfigure.env() != Environment.ONLINE:
        doc = '/doc/'
        version = '1.10.19'
        title = '某API接口管理程序'
        description = '用于展示接口'
        terms_url = ""
        contact = "showmove@qq.com"
        license = "Artwork License"
        license_url = 'https://flask.palletsprojects.com/en/2.2.x/license/#bsd-3-clause-source-license'
