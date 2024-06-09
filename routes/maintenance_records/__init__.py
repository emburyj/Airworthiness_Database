from flask import Blueprint

maintenance_records_blueprint = Blueprint('maintenance_records_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views