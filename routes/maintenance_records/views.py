from flask import render_template, redirect, flash, request, current_app
from flask_mysqldb import MySQL
from . import maintenance_records_blueprint

@maintenance_records_blueprint.route('/', methods=["POST", "GET"])
def Maintenance_Records():
    mysql = current_app.extensions['mysql']
    entities = ["Maintenance ID", "N Number", "Maintenance Date", "Maintenance Description"]
    # display models query
    query = ("SELECT Maintenance_Records.*, Registered_Aircraft.n_number FROM Maintenance_Records "
             "INNER JOIN Registered_Aircraft ON Registered_Aircraft.aircraft_id = Maintenance_Records.aircraft_id "
             "ORDER BY Registered_Aircraft.n_number")
    cur = mysql.connection.cursor()
    cur.execute(query)
    maintenance_data = cur.fetchall()

    if request.method == "POST":

        # Create New MD
        # if user presses Add button for new model
        if request.form.get("NewRecord"):
            # get the inputs and selects
            aircraft_id_select = str(request.form.get("NNumber"))
            date_input = request.form["RecordDate"]
            description_input = request.form["RecordDescription"]

            # data validation
            if date_input == "" or description_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Maintenance_Records')
            check_query = (f"SELECT * FROM Maintenance_Records WHERE aircraft_id = '{aircraft_id_select}' AND "
                           f"maintenance_date = '{date_input}' AND maintenance_description = '{description_input}'")
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Identical entry already exists! Please provide unique input.')
                return redirect('/Maintenance_Records')

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

            # data validation
            if date_input == "" or description_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Maintenance_Records')
            check_query = (f"SELECT * FROM Maintenance_Records WHERE aircraft_id = '{aircraft_id_select}' AND "
                           f"maintenance_date = '{date_input}' AND maintenance_description = '{description_input}' "
                           f"AND maintenance_id != {maintenance_id_select}")
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Identical entry already exists! Please provide unique input.')
                return redirect('/Maintenance_Records')

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

    return render_template("Maintenance_Records.html", entities=entities, data=maintenance_data,
                           page_name="Maintenance Records")