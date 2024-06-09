from flask import render_template, redirect, flash, request, current_app
from flask_mysqldb import MySQL
from . import registered_aircraft_blueprint

@registered_aircraft_blueprint.route('/', methods=["POST", "GET"])
def Registered_Aircraft():
    mysql = current_app.extensions['mysql']
    entities = ["Aircraft ID", "N Number", "Owner Name", "Model Name", "Current Status"]
    # if request.method == "GET":
    # display models query
    aircraft_query = (
        "SELECT Registered_Aircraft.*, Aircraft_Owners.owner_name, Aircraft_Models.model_name FROM Registered_Aircraft "
        "INNER JOIN Aircraft_Owners on Aircraft_Owners.owner_id = Registered_Aircraft.owner_id "
        "INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Registered_Aircraft.model_id "
        "ORDER BY Registered_Aircraft.n_number")
    owner_query = "SELECT * FROM Aircraft_Owners ORDER BY owner_name"
    model_query = "SELECT * FROM Aircraft_Models ORDER BY model_name"
    cur = mysql.connection.cursor()
    cur.execute(aircraft_query)
    aircraft_data = cur.fetchall()
    cur.execute(owner_query)
    owner_data = cur.fetchall()
    cur.execute(model_query)
    model_data = cur.fetchall()

    if request.method == "POST":

        # Create New Aircraft
        # if user presses Add button for new model
        if request.form.get("NewRegisteredAircraft"):
            # get the inputs and selects
            n_number_input = request.form["NNumber"]
            owner_id_select = str(request.form.get("AircraftOwner"))
            model_id_select = str(request.form.get("AircraftModel"))
            status_input = request.form["CurrentStatus"]

            # data validation
            if n_number_input == "" or status_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Registered_Aircraft')
            check_query = f"SELECT * FROM Registered_Aircraft WHERE n_number = '{n_number_input}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Please provide unique input!')
                return redirect('/Registered_Aircraft')

            # create new aircraft query
            query = "INSERT INTO Registered_Aircraft (n_number, owner_id, model_id, status) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (n_number_input, owner_id_select, model_id_select, status_input))
            mysql.connection.commit()

        # Update Aircraft
        # if user presses Update button
        if request.form.get("UpdateRegisteredAircraft"):
            aircraft_id_select = str(request.form.get("AircraftID"))
            n_number_input = request.form["NNumber"]
            owner_id_select = str(request.form.get("AircraftOwner"))
            model_id_select = str(request.form.get("AircraftModel"))
            status_input = request.form["CurrentStatus"]

            # data validation
            if n_number_input == "" or status_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Registered_Aircraft')
            check_query = f"SELECT * FROM Registered_Aircraft WHERE n_number = '{n_number_input}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Please provide unique input!')
                return redirect('/Registered_Aircraft')

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

    return render_template("Registered_Aircraft.html", entities=entities,
                           data={'aircraft_data': aircraft_data, 'owner_data': owner_data, 'model_data': model_data},
                           page_name="Registered Aircraft")