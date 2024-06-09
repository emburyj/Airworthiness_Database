from flask import Flask, render_template, redirect, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv, find_dotenv
import os

def build_app():
    app = Flask(__name__, static_folder='../static')

    load_dotenv(find_dotenv())

    # connect to the CS340 database
    # The following code was adapted from the CS340 starter project
    # Date 6/8/2024
    # Source: https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master?tab=readme-ov-file#our-initial-data-templates-and-html
    app.config['MYSQL_HOST'] = os.environ.get("340DBHOST")
    app.config['MYSQL_USER'] = os.environ.get("340DBUSER")
    app.config['MYSQL_PASSWORD'] = os.environ.get("340DBPW")
    app.config['MYSQL_DB'] = os.environ.get("340DB")
    app.config['MYSQL_CURSORCLASS'] = "DictCursor"
    app.secret_key = os.environ.get("SECRET_KEY")
    mysql = MySQL(app)
    app.extensions = {'mysql': mysql}

    # import blueprints from routes
    # The following code was adapted from the Flask project documentation/tutorial
    # Date 6/8/2024
    # Source: https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
    from routes.airworthiness_directives import airworthiness_directives_blueprint
    app.register_blueprint(airworthiness_directives_blueprint, url_prefix='/Airworthiness_Directives')

    from routes.registered_aircraft import registered_aircraft_blueprint
    app.register_blueprint(registered_aircraft_blueprint, url_prefix='/Registered_Aircraft')

    from routes.aircraft_models import aircraft_models_blueprint
    app.register_blueprint(aircraft_models_blueprint, url_prefix='/Aircraft_Models')

    from routes.aircraft_owners import aircraft_owners_blueprint
    app.register_blueprint(aircraft_owners_blueprint, url_prefix='/Aircraft_Owners')

    from routes.maintenance_records import maintenance_records_blueprint
    app.register_blueprint(maintenance_records_blueprint, url_prefix='/Maintenance_Records')

    from routes.models_directives import models_directives_blueprint
    app.register_blueprint(models_directives_blueprint, url_prefix='/Models_Directives')

    @app.route('/')
    def about():
        return render_template("about.html", page_name="Airworthiness Database")

    return app