from flask import Blueprint

aircraft_models_blueprint = Blueprint('aircraft_models_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views