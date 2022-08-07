

from config import *
import sys
from flask_cors import CORS
from flask import Blueprint, Flask
from flask_restplus import Api
from orm import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion, force_instant_defaults

cross_origin_resource_sharing = CORS()

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

app = Flask(__name__)

app.config.update(APP_SETTINGS.toObject())

# app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % (
#     os.path.join(PROJECT_ROOT, "example.db"))
db = SQLAlchemy(app)
force_auto_coercion()
force_instant_defaults()
app.secret_key = 'B0ZrPP9DW123j/3yX R~XHH!jmN]LWX/,?RT'
blues = Blueprint('api', __name__, url_prefix='/api')
api = Api(blues, **API_SETTING.toObject())
app.register_blueprint(blues)
