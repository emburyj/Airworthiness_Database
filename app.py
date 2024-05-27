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

    data = ()

    return render_template("Airworthiness_Directives.html", entities=entities, data=data, page_name="Airworthiness Directives")

@app.route('/Registered_Aircraft')
def Registered_Aircraft():
    entities = ["Aircraft ID", "N Number", "Owner ID","Owner Name", "Model ID","Model Name", "Current Status"]
    data = ()

    return render_template("Registered_Aircraft.html",entities=entities, data=data, page_name="Registered Aircraft")

@app.route('/Aircraft_Models')
def Aircraft_Models():
    entities = ["Model ID", "Manufacturer Name", "Model Name"]
    # if request.method == "GET":
    # display models query
    query = "SELECT * FROM Aircraft_Models ORDER BY model_name;"
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

    data = []

    return render_template("Maintenance_Records.html", entities=entities, data=data, page_name="Maintenance Records")

@app.route('/Models_Directives')
def Models_Directives():
    entities = ["Models Directives ID", "Model ID", "Model Name", "AD ID", "Airworthiness Directive Number"]

    data = []

    return render_template("Models_Directives.html", entities=entities, data=data, page_name="Models Impacted by Directives")


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=2468, debug=False)
