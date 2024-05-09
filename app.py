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
    entities = ["N Number", "Owner Name", "Model Name", "Current Status"]
    data = {
            "Owners": ["Josh Embury", "Ian Bubier", "United Airlines", "Alaska Airlines"],
            "Models": ["737-8", "737-9", "A320-214", "E1000"],
            "Aircraft": [
                        {"Number": "N921AK", "Owner": "Josh Embury", "Model": "737-9", "Status": "Grounded for Maintenance"},
                        {"Number": "N200MR", "Owner": "Ian Bubier", "Model": "E1000", "Status": "In-Service"},
                        {"Number": "N291BT", "Owner": "Alaska Airlines", "Model": "737-9", "Status": "Pending Maintenance"},
                        ]
            }
    return render_template("Registered_Aircraft.html",entities=entities, data=data, page_name="Registered Aircraft")

@app.route('/Aircraft_Models')
def Aircraft_Models():
    entities = ["Manufacturer Name", "Model Name"]
    model_data = [
                    {"Manufacturer": "The Boeing Company", "Model": "737-8"},
                    {"Manufacturer": "The Boeing Company", "Model": "737-9"},
                    {"Manufacturer": "Airbus SAS", "Model": "A320-214"},
                    {"Manufacturer": "Epic Aircraft", "Model": "E1000"}
                ]
    return render_template("Aircraft_Models.html", entities=entities, data=model_data, page_name="Aircraft Models")

@app.route('/Aircraft_Owners')
def Aircraft_Owners():
    entities = ["Owner Name", "Owner Email Address"]
    owner_data = [
                    {"Name": "Josh Embury", "Email": "emburyj@oregonstate.edu"},
                    {"Name": "Ian Bubier", "Email": "bubieri@oregonstate.edu"},
                    {"Name": "United Airlines", "Email": "therealunited@aol.com"},
                    {"Name": "Alaska Airlines", "Email": "alaskaair@hotmail.com"}
                ]

    return render_template("Aircraft_Owners.html", entities=entities, data=owner_data, page_name="Aircraft Owners")

@app.route('/Maintenance_Records')
def Maintenance_Records():

    return render_template("Maintenance_Records.html", page_name="Maintenance Records")

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=3000, debug=True)
