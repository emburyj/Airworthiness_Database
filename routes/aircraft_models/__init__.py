from flask import Blueprint
    # The following code was adapted from the Flask project documentation/tutorial
    # Date 6/8/2024
    # Source: https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
aircraft_models_blueprint = Blueprint('aircraft_models_blueprint', __name__, template_folder='../../templates', static_folder='../../static')
from . import views