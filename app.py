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
    entities = ["AD ID", "Airworthiness Directive Number",
                 "Airworthiness Directive Description", "Maintenance Required Date"]
    desc = [
            """The loss of the SPCU and ground through the P6 panel could result
            in the loss of significant flightcrew instrumentation and displays.
            This AD requires installing two bonding jumpers from the P6 panel
            structure to primary structure.""",
            """This emergency AD was prompted by a report of an in-flight departure
                of a mid cabin door plug, which resulted in a rapid decompression of
                the airplane. The FAA is issuing this AD to address the potential
                in-flight loss of a mid cabin door plug, which could result in injury
                to passengers and crew, the door impacting the airplane, and/or loss
                of control of the airplane.""",
                """To address incomplete installations of the over wing panel lug attachments
                in the production assembly line, which, if not detected and corrected, could
                reduce the structural integrity of the wing."""
            ]

    data = [
            {"ID": 1, "Number": "2024-06-03", "Description": desc[0], "Date": "2024-05-02"},
            {"ID": 2, "Number": "2024-02-51_Emergency", "Description": desc[1], "Date": "2024-01-06"},
            {"ID": 3, "Number": "2024-06-07", "Description": desc[2], "Date": "2024-05-22"},
    ]

    return render_template("Airworthiness_Directives.html", entities=entities, data=data, page_name="Airworthiness Directives")

@app.route('/Registered_Aircraft')
def Registered_Aircraft():
    entities = ["Aircraft ID", "N Number", "Owner ID","Owner Name", "Model ID","Model Name", "Current Status"]
    data = {
            "Owners": ["Josh Embury", "Ian Bubier", "United Airlines", "Alaska Airlines"],
            "Models": ["737-8", "737-9", "A320-214", "E1000"],
            "Aircraft": [
                        {"ID": 1, "Number": "N921AK", "OID": 1,"Owner": "Josh Embury", "MID": 2, "Model": "737-9", "Status": "Grounded for Maintenance"},
                        {"ID": 2, "Number": "N200MR", "OID": 2,"Owner": "Ian Bubier", "MID": 4, "Model": "E1000", "Status": "In-Service"},
                        {"ID": 3, "Number": "N291BT", "OID": 4,"Owner": "Alaska Airlines", "MID": 2, "Model": "737-9", "Status": "Pending Maintenance"},
                        ]
            }
    return render_template("Registered_Aircraft.html",entities=entities, data=data, page_name="Registered Aircraft")

@app.route('/Aircraft_Models')
def Aircraft_Models():
    entities = ["Model ID", "Manufacturer Name", "Model Name"]
    model_data = [
                    {"ID": 1, "Manufacturer": "The Boeing Company", "Model": "737-8"},
                    {"ID": 2, "Manufacturer": "The Boeing Company", "Model": "737-9"},
                    {"ID": 3, "Manufacturer": "Airbus SAS", "Model": "A320-214"},
                    {"ID": 4, "Manufacturer": "Epic Aircraft", "Model": "E1000"}
                ]
    return render_template("Aircraft_Models.html", entities=entities, data=model_data, page_name="Aircraft Models")

@app.route('/Aircraft_Owners')
def Aircraft_Owners():
    entities = ["Owner ID", "Owner Name", "Owner Email Address"]
    owner_data = [
                    {"ID": 1, "Name": "Josh Embury", "Email": "emburyj@oregonstate.edu"},
                    {"ID": 2, "Name": "Ian Bubier", "Email": "bubieri@oregonstate.edu"},
                    {"ID": 3, "Name": "United Airlines", "Email": "therealunited@aol.com"},
                    {"ID": 4, "Name": "Alaska Airlines", "Email": "alaskaair@hotmail.com"}
                ]

    return render_template("Aircraft_Owners.html", entities=entities, data=owner_data, page_name="Aircraft Owners")

@app.route('/Maintenance_Records')
def Maintenance_Records():
    entities = ["Maintenance ID", "Aircraft ID", "Maintenance Date", "Maintenance Description"]

    data = [
            {"MID": 1, "AID": 1, "Date": "2018-10-30", "Description": "Fixed a thing."},
            {"MID": 2, "AID": 1, "Date": "2019-01-15", "Description": "Repaired a doodad."},
            {"MID": 3, "AID": 1, "Date": "2021-06-18", "Description": "Mended a thingamajig."},
            {"MID": 4, "AID": 2, "Date": "2023-07-29", "Description": "Reconfigured a whotsit."},
            {"MID": 5, "AID": 3, "Date": "2024-01-05", "Description": "Jury-rigged a whatchamacallit."}
            ]

    return render_template("Maintenance_Records.html", entities=entities, data=data, page_name="Maintenance Records")

@app.route('/Models_Directives')
def Models_Directives():
    entities = ["Models Directives ID", "Model ID", "AD ID"]

    data = [
            {"MDID": 1, "MID": 2, "ADID": 2},
            {"MDID": 2, "MID": 1, "ADID": 1},
            {"MDID": 3, "MID": 2, "ADID": 1},
            {"MDID": 4, "MID": 3, "ADID": 3}
            ]

    return render_template("Models_Directives.html", entities=entities, data=data, page_name="Maintenance Records")


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=2468, debug=False)
