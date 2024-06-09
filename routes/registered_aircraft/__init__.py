from flask import Blueprint

registered_aircraft_blueprint = Blueprint('registered_aircraft_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views