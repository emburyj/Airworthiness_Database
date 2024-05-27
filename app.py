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
    entities = ["Airworthiness Directive ID", "Airworthiness Directive Number", "Airworthiness Directive Description", "Maintenance Required Date"]
    # if request.method == "GET":
    # display ADs query
    query = "SELECT * FROM Airworthiness_Directives ORDER BY ad_number"
    cur = mysql.connection.cursor()
    cur.execute(query)
    ad_data = cur.fetchall()

    if request.method == "POST":
        # Create New AD
        # if user presses Add button for new model

        if request.form.get("NewAd"):
            # get the inputs from text boxes
            ad_number_input = request.form["DirectiveNumber"]
            ad_description_input = request.form["DirectiveDescription"]
            required_maintenance_input = request.form["DirectiveDate"]
            # create new AD query
            query = "INSERT INTO Airworthiness_Directives (ad_number, ad_description, maintenance_required_date) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (ad_number_input, ad_description_input, required_maintenance_input))
            mysql.connection.commit()

        # Update AD
        # if user presses Update button
        if request.form.get("UpdateAD"):
            ad_id_select = str(request.form.get("ADID"))
            ad_number_input = request.form["DirectiveNumber"]
            ad_description_input = request.form["DirectiveDescription"]
            required_maintenance_input = request.form["DirectiveDate"]
            # update AD query
            query = "UPDATE Airworthiness_Directives SET ad_number = %s, ad_description = %s, maintenance_required_date WHERE ad_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (ad_number_input, ad_description_input, required_maintenance_input, ad_id_select))
            mysql.connection.commit()

        # Delete AD
        # if user presses Delete button
        if request.form.get("DeleteAD"):
            ad_id_select = str(request.form.get("ADID"))
            # delete AD query
            query = f"DELETE FROM Airworthiness_Directives WHERE ad_id = '{ad_id_select}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Airworthiness_Directives')

    return render_template("Airworthiness_Directives.html", entities=entities, data=ad_data, page_name="Airworthiness Directives")

@app.route('/Registered_Aircraft')
def Registered_Aircraft():
    entities = ["Aircraft ID", "N Number", "Owner Name", "Model Name", "Current Status"]
    # if request.method == "GET":
    # display models query
    query = ("SELECT Registered_Aircraft.*, Aircraft_Owners.owner_name, Aircraft_Models.model_name FROM Registered_Aircraft"
             "INNER JOIN Aircraft_Owners on Aircraft_Owners.owner_id = Registered_Aircraft.owner_id"
             "INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Registered_Aircraft = model_id"
             "ORDER BY model_name")
    cur = mysql.connection.cursor()
    cur.execute(query)
    aircraft_data = cur.fetchall()

    if request.method == "POST":

        # Create New Aircraft
        # if user presses Add button for new model
        if request.form.get("NewRegisteredAircraft"):
            # get the inputs from text boxes
            n_number_input = request.form["NNumber"]
            owner_id_select = request.form["AircraftOwner"]
            model_id_select = request.form["AircraftModel"]
            status_input = request.form["CurrentStatus"]
            # create new aircraft query
            query = "INSERT INTO Registered_Aircraft (n_number_input, owner_id_select, model_id_select, status_input) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (n_number_input, owner_id_select, model_id_select, status_input))
            mysql.connection.commit()

        # Update Aircraft
        # if user presses Update button
        if request.form.get("UpdateRegisteredAircraft"):
            aircraft_id_select = str(request.form.get("AircraftID"))
            n_number_input = request.form["NNumber"]
            owner_id_select = request.form["AircraftOwner"]
            model_id_select = request.form["AircraftModel"]
            status_input = request.form["CurrentStatus"]
            # update aircraft query
            query = "UPDATE Registered_Aircraft SET n_number = %s, owner_id = %s, model_id = %s, status = %s WHERE aircraft_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (n_number_input, owner_id_select, model_id_select, status_input, aircraft_id_select))
            mysql.connection.commit()

        # Delete Aircraft
        # if user presses Delete button
        if request.form.get("DeleteRegisteredAircraft"):
            aircraft_id_select = str(request.form.get("AircraftID"))
            # delete aircraft query
            query = f"DELETE FROM Registered_Aircraft WHERE aircraft_id = '{aircraft_id_select}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Registered_Aircraft')

    return render_template("Registered_Aircraft.html",entities=entities, data=aircraft_data, page_name="Registered Aircraft")

@app.route('/Aircraft_Models')
def Aircraft_Models():
    entities = ["Model ID", "Manufacturer Name", "Model Name"]
    # if request.method == "GET":
    # display models query
    query = "SELECT * FROM Aircraft_Models ORDER BY model_name"
    cur = mysql.connection.cursor()
    cur.execute(query)
    model_data = cur.fetchall()

    if request.method == "POST":

        # Create New Model
        # if user presses Add button for new model
        if request.form.get("NewAircraftModel"):
            # get the inputs from text boxes
            manufacturer_name_input = request.form["AircraftManufacturer"]
            model_name_input = request.form["AircraftModel"]
            # create new model query
            query = "INSERT INTO Aircraft_Models (manufacturer_name, model_name) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (manufacturer_name_input, model_name_input))
            mysql.connection.commit()

        # Update Model
        # if user presses Update button
        if request.form.get("UpdateAircraftModel"):
            model_id_select = str(request.form.get("ModelID"))
            manufacturer_name_input = request.form["AircraftManufacturer"]
            model_name_input = request.form["AircraftModel"]
            # update model query
            query = "UPDATE Aircraft_Models SET manufacturer_name = %s, model_name = %s WHERE model_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (manufacturer_name_input, model_name_input, model_id_select))
            mysql.connection.commit()

        # Delete Model
        # if user presses Delete button
        if request.form.get("DeleteAircraftModel"):
            model_id_select = str(request.form.get("ModelID"))
            # delete model query
            query = f"DELETE FROM Aircraft_Models WHERE model_id = '{model_id_select}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Aircraft_Models')

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
            query = "UPDATE Aircraft_Owners SET owner_name = %s, owner_email = %s WHERE owner_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (owner_name_input, owner_email_input, dropdown_name))
            mysql.connection.commit()

        # Delete Owner
        # if user presses Delete button
        if request.form.get("DeleteOwner"):
            dropdown_name = str(request.form.get("OwnerDropdownName"))
            # delete owner query
            query = f"DELETE FROM Aircraft_Owners WHERE owner_id = '{dropdown_name}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Aircraft_Owners')

    return render_template("Aircraft_Owners.html", entities=entities, data=owner_data, page_name="Aircraft Owners")

@app.route('/Maintenance_Records')
def Maintenance_Records():
    entities = ["Maintenance ID", "N Number", "Maintenance Date", "Maintenance Description"]
    # display models query
    query = ("SELECT Maintenance_Records.*, Registered_Aircraft.n_number FROM Maintenance_Records"
             "INNER JOIN Registered_Aircraft ON Registered_Aircraft.aircraft_id = Maintenance_Records.aircraft_id"
             "ORDER BY Registered_Aircraft")
    cur = mysql.connection.cursor()
    cur.execute(query)
    maintenance_data = cur.fetchall()

    if request.method == "POST":

        # Create New MD
        # if user presses Add button for new model
        if request.form.get("NewRecord"):
            # get the inputs from text boxes
            aircraft_id_select = str(request.form.get("NNumber"))
            date_input = request.form["RecordDate"]
            description_input = request.form["RecordDescription"]
            # create new md query
            query = "INSERT INTO Maintenance_Records (aircraft_id, maintenance_date, maintenance_description) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (aircraft_id_select, date_input, description_input))
            mysql.connection.commit()

        # Update MD
        # if user presses Update button
        if request.form.get("UpdateRecord"):
            maintenance_id_select = str(request.form.get("RecordID"))
            aircraft_id_select = str(request.form.get("NNumber"))
            date_input = request.form["RecordDate"]
            description_input = request.form["RecordDescription"]
            # update md query
            query = "UPDATE Maintenance_Records SET aircraft_id = %s, maintenance_date = %s, maintenance_description = %s WHERE maintenance_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (aircraft_id_select, date_input, description_input, maintenance_id_select))
            mysql.connection.commit()

        # Delete MD
        # if user presses Delete button
        if request.form.get("DeleteRecord"):
            maintenance_id_select = str(request.form.get("RecordID"))
            # delete md query
            query = f"DELETE FROM Maintenance_Records WHERE maintenance_id = '{maintenance_id_select}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Maintenance_Records')

    return render_template("Maintenance_Records.html", entities=entities, data=maintenance_data, page_name="Maintenance Records")

@app.route('/Models_Directives')
def Models_Directives():
    entities = ["Models Directives ID", "Model Name", "Airworthiness Directive Number"]    # if request.method == "GET":
    # display models query
    query = ("SELECT Models_Directives.*, Aircraft_Models.model_name, Airworthiness_Directives.ad_number FROM Models_Directives"
             "INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Models_Directives.model_id"
             "INNER JOIN Airworthiness_Directives ON Airworthiness_Directives.ad_id = Models_Directives.ad_id"
             "ORDER BY Models_Directives.md_id")
    cur = mysql.connection.cursor()
    cur.execute(query)
    md_data = cur.fetchall()

    if request.method == "POST":

        # Create New MD
        # if user presses Add button for new model
        if request.form.get("NewMD"):
            # get the inputs from text boxes
            model_id_select = request.form["ModelID"]
            ad_id_select = request.form["ADID"]
            # create new md query
            query = "INSERT INTO Models_Directives (model_id, ad_id) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (model_id_select, ad_id_select))
            mysql.connection.commit()

        # Update MD
        # if user presses Update button
        if request.form.get("UpdateMD"):
            md_id_select = str(request.form.get("MDID"))
            model_id_select = request.form["ModelID"]
            ad_id_select = request.form["ADID"]
            # update md query
            query = "UPDATE Models_Directives SET model_id = %s, ad_id = %s WHERE md_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (model_id_select, ad_id_select, md_id_select))
            mysql.connection.commit()

        # Delete MD
        # if user presses Delete button
        if request.form.get("DeleteMD"):
            md_id_select = str(request.form.get("MDID"))
            # delete md query
            query = f"DELETE FROM Models_Directives WHERE md_id = '{md_id_select}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Models_Directives')

    return render_template("Models_Directives.html", entities=entities, data=md_data, page_name="Models Impacted by Directives")


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=2468, debug=False)
