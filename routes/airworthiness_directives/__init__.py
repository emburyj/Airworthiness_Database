from flask import Blueprint

airworthiness_directives_blueprint = Blueprint('airworthiness_directives_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views