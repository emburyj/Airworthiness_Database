from flask import Blueprint

models_directives_blueprint = Blueprint('models_directives_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views