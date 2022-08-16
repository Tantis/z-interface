

import time
import random
from config import *
import sys
from flask_cors import CORS
from flask import Blueprint, Flask, jsonify
from flask_restplus import Api
from orm import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion, force_instant_defaults
from tasks.celery import createCelery


if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config.update(APP_SETTINGS.toJson())
db = SQLAlchemy(app)
force_auto_coercion()
force_instant_defaults()
app.secret_key = 'B0ZrPP9DW123j/3yX R~XHH!jmN]LWX/,?RT'
blues = Blueprint('api', __name__, url_prefix='/api')
api = Api(blues, **API_SETTING.toJson())
app.register_blueprint(blues)
celery = createCelery(app)
cross_origin_resource_sharing = CORS(
    app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', methods=['GET', "POST"])
def hello_world():
    celery_id = celery._common_task_list.collect.long_task.apply_async()
    return "<a href={}>查看执行状态!<h1>".format('/status/' + str(celery_id))


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = celery._common_task_list.collect.long_task.AsyncResult(
        task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),
        }
    return jsonify(response)
