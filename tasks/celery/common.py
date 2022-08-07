from .task import CeleryCommon
from config import CeleryConfig
__all__ = ["createCelery"]


def createCelery(app):

    celery_app = CeleryCommon(app.import_name)
    celery_app.config_from_object(CeleryConfig)
    return celery_app
