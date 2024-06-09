from flask import render_template, redirect, flash, request, current_app
from flask_mysqldb import MySQL
from . import aircraft_models_blueprint

@aircraft_models_blueprint.route('/', methods=["POST", "GET"])
def Aircraft_Models():
    mysql = current_app.extensions['mysql']
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
            # get the inputs and selects
            manufacturer_name_input = request.form["AircraftManufacturer"]
            model_name_input = request.form["AircraftModel"]

            # data validation
            if manufacturer_name_input == "" or model_name_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Aircraft_Models')
            check_query = f"SELECT 1 FROM Aircraft_Models WHERE model_name = '{model_name_input}'"
            cur.execute(check_query)
            if cur.fetchall() is not False:
                flash('Error: Please provide unique input!')
                return redirect('/Aircraft_Models')

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

            # data validation
            if manufacturer_name_input == "" or model_name_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Aircraft_Models')
            check_query = f"SELECT 1 FROM Aircraft_Models WHERE model_name = '{model_name_input}'"
            cur.execute(check_query)
            if cur.fetchall() is not False:
                flash('Error: Please provide unique input!')
                return redirect('/Aircraft_Models')

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