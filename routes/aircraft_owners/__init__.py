from flask import Blueprint

aircraft_owners_blueprint = Blueprint('aircraft_owners_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views