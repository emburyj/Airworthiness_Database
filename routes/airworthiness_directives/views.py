from flask import render_template, redirect, flash, request, current_app
from flask_mysqldb import MySQL
from . import airworthiness_directives_blueprint

@airworthiness_directives_blueprint.route('/', methods=["POST", "GET"])
def Airworthiness_Directives():
    mysql = current_app.extensions['mysql']
    entities = ["Airworthiness Directive ID", "Airworthiness Directive Number", "Airworthiness Directive Description",
                "Maintenance Required Date"]
    # if request.method == "GET":
    # display ADs query
    query = "SELECT * FROM Airworthiness_Directives ORDER BY ad_number"
    cur = mysql.connection.cursor()
    cur.execute(query)
    ad_data = cur.fetchall()

    if request.method == "POST":
        # Create New AD
        # if user presses Add button for new model

        if request.form.get("NewAD"):
            # get the inputs and selects
            ad_number_input = request.form["DirectiveNumber"].strip()
            ad_description_input = request.form["DirectiveDescription"].strip()
            required_maintenance_input = request.form["DirectiveDate"].strip()

            # data validation
            if ad_number_input == "" or ad_description_input == "" or required_maintenance_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Airworthiness_Directives')
            check_query = f"SELECT * FROM Airworthiness_Directives WHERE ad_number = '{ad_number_input}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: AD Number already exists! Please provide unique input.')
                return redirect('/Airworthiness_Directives')

            # create new AD query
            query = "INSERT INTO Airworthiness_Directives (ad_number, ad_description, maintenance_required_date) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (ad_number_input, ad_description_input, required_maintenance_input))
            mysql.connection.commit()

        # Update AD
        # if user presses Update button
        if request.form.get("UpdateAD"):
            ad_id_select = str(request.form.get("ADID")).strip()
            ad_number_input = request.form["DirectiveNumber"].strip()
            ad_description_input = request.form["DirectiveDescription"].strip()
            required_maintenance_input = request.form["DirectiveDate"].strip()

            # data validation
            if ad_number_input == "" or ad_description_input == "" or required_maintenance_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Airworthiness_Directives')
            check_query = f"SELECT * FROM Airworthiness_Directives WHERE ad_number = '{ad_number_input}' AND ad_id != {ad_id_select}"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: AD Number already exists! Please provide unique input.')
                return redirect('/Airworthiness_Directives')

            # update AD query
            query = "UPDATE Airworthiness_Directives SET ad_number = %s, ad_description = %s, maintenance_required_date = %s WHERE ad_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (ad_number_input, ad_description_input, required_maintenance_input, ad_id_select))
            mysql.connection.commit()

        # Delete AD
        # if user presses Delete button
        if request.form.get("DeleteAD"):
            ad_id_select = str(request.form.get("ADID")).strip()
            # delete AD query
            query = f"DELETE FROM Airworthiness_Directives WHERE ad_id = '{ad_id_select}'"
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        # refresh page after post
        return redirect('/Airworthiness_Directives')

    return render_template("Airworthiness_Directives.html", entities=entities, data=ad_data,
                           page_name="Airworthiness Directives")