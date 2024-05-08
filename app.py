from flask import Flask, render_template, json, redirect
# from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
# app.config['MYSQL_USER'] = '' # TBD
# app.config['MYSQL_PASSWORD'] = '' # TBD
# app.config['MYSQL_DB'] = '' # TBD
# app.config['MYSQL_CURSORCLASS'] = "DictCursor"


# mysql = MySQL(app)



# Routes
@app.route('/')
def about():

    return render_template("about.html", page_name="Airworthiness Database")

@app.route('/Airworthiness_Directives')
def Airworthiness_Directives():

    return render_template("Airworthiness_Directives.html", page_name="Airworthiness Directives")

@app.route('/Registered_Aircraft')
def Registered_Aircraft():

    return render_template("Registered_Aircraft.html", page_name="Registered Aircraft")

@app.route('/Aircraft_Models')
def Aircraft_Models():

    return render_template("Aircraft_Models.html", page_name="Aircraft Models")

@app.route('/Aircraft_Owners')
def Aircraft_Owners():

    return render_template("Aircraft_Owners.html", page_name="Aircraft Owners")

@app.route('/Maintenance_Records')
def Maintenance_Records():

    return render_template("Maintenance_Records.html", page_name="Maintenance Records")

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=3000, debug=True)
