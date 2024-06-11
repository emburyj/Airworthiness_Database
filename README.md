# CS340 database project
# Airworthiness Database

## Overview
The Airworthiness Database is a web application to enable tracking the records of aircraft which are registered with the FAA, and to help identify required maintenance that is mandated by Airworthiness Directives issued by the FAA. The user interface is designed to facilitate Create, Read, Update, and Delete (CRUD) operations to be carried out by the database administrator. The application is built with Flask, the python web framework, and is connected to a MySQL database.

## Features
- Maintain contact information for Aircraft Owners
- Create and revise information related to Aircraft Models and Aircraft registered with the FAA.
- Apply FAA-mandated maintenance requirements to Registered Aircraft
- Track maintenance records for Registered Aircraft

## Installation
1. Clone the Airworthiness_Database repository from GitHub:
    ```
    git clone https://github.com/<your_username>/Airworthiness_Database.git
    ```
2. Create and activate virtual environment (optional):
    ```
    python3 -m venv projectenv
    source projectenv/bin/activate
    ```

3. Navigate to the locally-cloned repository and install dependencies:
    ```
    cd Airworthiness_Database
    pip3 install -r requirements.txt
    ```

## Running the Program
1. In the terminal, run the program:
    ```
    python3 app.py
    ```

2. View the application in your browser by navigating to the address:
    ```
    http://localhost:2468/
    ```

## Citations
- The code for this application was developed by Ian Bubier and Josh Embury with guidance from the Oregon State University CS340 course material.
- Changes were made to the application as a result of valuable feedback received by Justin Dickerson (TA) and by Peer Reviewers in the CS340 course.
- Project was organized/modularized using code adapted from the Flask project documentation: https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
- Code for connecting to and interacting with the MySQL database was adapted from the CS340 starter app: https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master?tab=readme-ov-file#our-initial-data-templates-and-html
