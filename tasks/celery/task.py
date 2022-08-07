
import random
import time
from interface.logger import logger
from celery import Celery
from celery import Task
from celery.worker.request import Request
from .taskController import collect


class MyRequest(Request):
    'A minimal custom request to log failures and hard time limits.'

    def on_timeout(self, soft, timeout):
        super(MyRequest, self).on_timeout(soft, timeout)
        if not soft:
            logger.warning(
                'A hard timeout was enforced for task %s',
                self.task.name
            )

    def on_failure(self, exc_info, send_failed_event=True, return_ok=False):
        super().on_failure(
            exc_info,
            send_failed_event=send_failed_event,
            return_ok=return_ok
        )
        logger.warning(
            'Failure detected for task %s',
            self.task.name
        )


class CeleryCommon(Celery):

    def on_init(self):
        logger.info("[celery][on_init] 初始化celery")
        super(CeleryCommon, self).on_init()
        self._common_task_list = CommonTask(self)

    def task(self, *args, **opts):
        logger.info("[celery][task] ")
        return super(CeleryCommon, self).task(*args, **opts)

    def register_task(self, task, **options):
        logger.info("[celery][register_task] ")
        return super(CeleryCommon, self).register(task, **options)


class MyTask(Task):
    Request = MyRequest  # you can use a FQN 'my.package:MyRequest'


class CommonTask:

    def __init__(self, celery):
        self.celery = celery
        self.collect = self.TaskController()

    def TaskController(self):
        """返回任务列表

        """
        return collect(self.celery)
