from flask import Blueprint
    # The following code was adapted from the Flask project documentation/tutorial
    # Date 6/8/2024
    # Source: https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
maintenance_records_blueprint = Blueprint('maintenance_records_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views