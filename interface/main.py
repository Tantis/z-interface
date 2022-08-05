
import os
import sys
from flask import Markup
from flask_cors import CORS
from flask import Blueprint, Flask, jsonify, url_for, render_template
from flask_restplus import Api
from orm import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion, force_instant_defaults
cross_origin_resource_sharing = CORS()

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % (
    os.path.join(PROJECT_ROOT, "example.db"))
db = SQLAlchemy(app)
force_auto_coercion()
force_instant_defaults()

app.secret_key = 'B0ZrPP9DW123j/3yX R~XHH!jmN]LWX/,?RT'
blues = Blueprint('api', __name__, url_prefix='/api')
api = Api(blues,
          doc='/doc/',  # 该选项为指定的文档地址
          # doc=False,  # 该选项未不开启文档
          version='1.10.19',
          title=u'管理后台',
          description=u'管理后台')
app.register_blueprint(blues)
