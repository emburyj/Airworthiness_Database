from flask import render_template, redirect, flash, request, current_app
from flask_mysqldb import MySQL
from . import aircraft_owners_blueprint

@aircraft_owners_blueprint.route('/', methods=["POST", "GET"])
def Aircraft_Owners():
    mysql = current_app.extensions['mysql']
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
            # get the inputs and selects
            owner_name_input = request.form["OwnerName"]
            owner_email_input = request.form["OwnerEmail"]

            # data validation
            if owner_name_input == "" or owner_email_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Aircraft_Owners')
            check_query = f"SELECT * FROM Aircraft_Owners WHERE owner_name = '{owner_name_input}' AND owner_email = '{owner_email_input}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Please provide unique input!')
                return redirect('/Aircraft_Owners')

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

            # data validation
            if owner_name_input == "" or owner_email_input == "":
                flash('Error: Please provide valid input!')
                return redirect('/Aircraft_Owners')
            check_query = f"SELECT * FROM Aircraft_Owners WHERE owner_name = '{owner_name_input}' AND owner_email = '{owner_email_input}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Please provide unique input!')
                return redirect('/Aircraft_Owners')

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