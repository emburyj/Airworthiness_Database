from flask import render_template, redirect, flash, request, current_app
from flask_mysqldb import MySQL
from . import models_directives_blueprint

@models_directives_blueprint.route('/', methods=["POST", "GET"])
def Models_Directives():
    mysql = current_app.extensions['mysql']
    entities = ["Models Directives ID", "Model Name", "Airworthiness Directive Number"]  # if request.method == "GET":
    # display models query
    query = (
        "SELECT Models_Directives.*, Aircraft_Models.model_name, Airworthiness_Directives.ad_number FROM Models_Directives "
        "INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Models_Directives.model_id "
        "INNER JOIN Airworthiness_Directives ON Airworthiness_Directives.ad_id = Models_Directives.ad_id "
        "ORDER BY Models_Directives.model_id")
    cur = mysql.connection.cursor()
    cur.execute(query)
    md_data = cur.fetchall()

    query = "SELECT * FROM Aircraft_Models"
    cur = mysql.connection.cursor()
    cur.execute(query)
    model_data = cur.fetchall()

    query = "SELECT * FROM Airworthiness_Directives"
    cur = mysql.connection.cursor()
    cur.execute(query)
    ad_data = cur.fetchall()

    if request.method == "POST":

        # Create New MD
        # if user presses Add button for new model
        if request.form.get("NewMD"):
            # get the inputs and selects
            model_id_select = str(request.form.get("ModelID"))
            ad_id_select = str(request.form.get("ADID"))

            # data validation
            check_query = f"SELECT * FROM Models_Directives WHERE model_id = '{model_id_select}' AND ad_id = '{ad_id_select}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Please provide unique input!')
                return redirect('/Models_Directives')

            # create new md query
            query = "INSERT INTO Models_Directives (model_id, ad_id) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (model_id_select, ad_id_select))
            mysql.connection.commit()

        # Update MD
        # if user presses Update button
        if request.form.get("UpdateMD"):
            md_id_select = str(request.form.get("MDID"))
            model_id_select = str(request.form.get("ModelID"))
            ad_id_select = str(request.form.get("ADID"))

            # data validation
            check_query = f"SELECT * FROM Models_Directives WHERE model_id = '{model_id_select}' AND ad_id = '{ad_id_select}'"
            cur.execute(check_query)
            if cur.fetchall():
                flash('Error: Please provide unique input!')
                return redirect('/Models_Directives')

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

    return render_template("Models_Directives.html", entities=entities,
                           data=md_data, models=model_data, ADs=ad_data, page_name="Models Impacted by Directives")