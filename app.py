from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)

load_dotenv(find_dotenv())

app.config['MYSQL_HOST'] = os.environ.get("340DBHOST")
app.config['MYSQL_USER'] = os.environ.get("340DBUSER")
app.config['MYSQL_PASSWORD'] = os.environ.get("340DBPW")
app.config['MYSQL_DB'] = os.environ.get("340DB")
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)



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

@app.route('/Aircraft_Owners', methods=["POST", "GET"])
def Aircraft_Owners():
    entities = ["Owner ID", "Owner Name", "Owner Email Address"]
    # if request.method == "GET":
    # display owners query
    query1 = "SELECT * FROM Aircraft_Owners ORDER BY owner_name;"
    cur = mysql.connection.cursor()
    cur.execute(query1)
    owner_data = cur.fetchall()


    if request.method == "POST":
        # Create New Owner
        # if user presses Add button for new owner
        if request.form.get("NewOwner"):
            # get the inputs from text boxes
            owner_name_input = request.form["OwnerName"]
            owner_email_input = request.form["OwnerEmail"]

            # create new owner query
            query = "INSERT INTO Aircraft_Owners (owner_name, owner_email) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (owner_name_input, owner_email_input))
            mysql.connection.commit()

        # Update Owner
        # if user presses Update button
        if request.form.get("UpdateOwner"):
            dropdown_name = str(request.form.get("OwnerDropdownName"))
            owner_name_input = request.form["OwnerName"]
            owner_email_input = request.form["OwnerEmail"]
            # update owner query
            query = "UPDATE Aircraft_Owners SET owner_name = %s, owner_email = %s WHERE owner_name = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (owner_name_input, owner_email_input, dropdown_name))
            mysql.connection.commit()

        # Delete Owner
        # if user presses Delete button
        if request.form.get("DeleteOwner"):
            dropdown_name = str(request.form.get("OwnerDropdownName"))
            # delete owner query
            query = f"DELETE FROM Aircraft_Owners WHERE owner_name = '{dropdown_name}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Aircraft_Owners')

    return render_template("Aircraft_Owners.html", entities=entities, data=owner_data, page_name="Aircraft Owners")

@app.route('/Maintenance_Records')
def Maintenance_Records():
    entities = ["Maintenance ID", "Aircraft ID", "N Number", "Maintenance Date", "Maintenance Description"]

    data = [
            {"MID": 1, "AID": 1, "Number": "N921AK", "Date": "2018-10-30", "Description": "Fixed a thing."},
            {"MID": 2, "AID": 1, "Number": "N921AK", "Date": "2019-01-15", "Description": "Repaired a doodad."},
            {"MID": 3, "AID": 1, "Number": "N921AK", "Date": "2021-06-18", "Description": "Mended a thingamajig."},
            {"MID": 4, "AID": 2, "Number": "N200MR", "Date": "2023-07-29", "Description": "Reconfigured a whatsit."},
            {"MID": 5, "AID": 3, "Number": "N291BT", "Date": "2024-01-05", "Description": "Jury-rigged a whatchamacallit."}
            ]

    return render_template("Maintenance_Records.html", entities=entities, data=data, page_name="Maintenance Records")

@app.route('/Models_Directives')
def Models_Directives():
    entities = ["Models Directives ID", "Model ID", "Model Name", "AD ID", "Airworthiness Directive Number"]

    data = [
            {"MDID": 1, "MID": 2, "Model": "737-9", "ADID": 2, "Number": "2024-02-51_Emergency"},
            {"MDID": 2, "MID": 1, "Model": "737-8", "ADID": 1, "Number": "2024-06-03"},
            {"MDID": 3, "MID": 2, "Model": "737-9", "ADID": 1, "Number": "2024-06-03"},
            {"MDID": 4, "MID": 3, "Model": "A320-214", "ADID": 3, "Number": "2024-06-07"}
            ]

    return render_template("Models_Directives.html", entities=entities, data=data, page_name="Models Impacted by Directives")


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=3000, debug=True)
