-- : used to denote variables with data from backend python application


-- INSERT QUERIES

-- add an aircraft owner
INSERT INTO Aircraft_Owners (owner_name, owner_email) VALUES (:owner_name_input, :owner_email_input)

-- add an aircraft model
INSERT INTO Aircraft_Models (manufacturer_name, model_name) VALUES (:manufacturer_name_input, :model_name_input)

-- add a registered aircraft
INSERT INTO Registered_Aircraft (n_number, owner_id, model_id, status) VALUES (:n_number_input, :owner_id_dropdown, :model_id_dropdown, status_input)
-- owner id is NULLable

-- add an airworthiness directive
INSERT INTO Airworthiness_Directives (ad_number, ad_description, maintenance_required_date) VALUES (:ad_number_input, :ad_description_input, :maintenance_required_date_input)

-- add a maintenance record
INSERT INTO Maintenance_Records (aircraft_id, maintenance_date, maintenance_description) VALUES (:aircraft_id_dropdown, :maintenance_date_input, :maintenance_description_input)

-- add a models directives relationship
INSERT INTO Models_Directives (model_id, ad_id) VALUES (:model_id_dropdown, :ad_id_dropdown)


-- DELETE QUERIES

-- delete an aircraft owner
DELETE FROM Aircraft_Owners WHERE owner_id = :selected_owner_id

-- delete an aircraft model
DELETE FROM Aircraft_Models WHERE model_id = :selected_model_id

-- delete a registered aircraft
DELETE FROM Registered_Aircraft WHERE aircraft_id = :selected_aircraft_id

-- delete airworthiness directive
DELETE FROM Airworthiness_Directives WHERE ad_id = :selected_ad_id

--delete a maintenance record
DELETE FROM Maintenance_Records WHERE maintenance_id = :selected_maintenance_id

--delete a models directives relationship
DELETE FROM Models_Directives WHERE model_id = :model_id_dropdown AND ad_id = :ad_id_dropdown


-- UPDATE QUERIES

-- update an aircraft owner
UPDATE Aircraft_Owners SET owner_name = :owner_name_input, owner_email = :owner_email_input WHERE owner_id = :selected_owner_id

-- update an aircraft model
UPDATE Aircraft_Models SET manufacturer_name = :manufacturer_name_input, model_name = :model_name_input WHERE model_id = :selected_model_id

-- update a registered aircraft
UPDATE Registered_Aircraft SET n_number = :n_number_input, owner_id = :owner_id_dropdown, model_id = :model_id_dropdown, status = :status_input WHERE aircraft_id = :selected_aircraft_id
-- owner id is NULLable

-- update an airworthiness directive
UPDATE Airworthiness_Directives SET ad_number = :ad_number_input, ad_description = :ad_description_input, maintenance_required_date = :maintenance_required_date_input WHERE ad_id = :selected_ad_id

-- update a maintenance record
UPDATE Maintenance_Records SET aircraft_id = :aircraft_id_dropdown, maintenance_date = :maintenance_date_input, maintenance_description = :maintenance_description_input WHERE maintenance_id = :selected_maintenance_id

-- update a models directives relationship
UPDATE Models_Directives SET model_id = :model_id_dropdown WHERE ad_id = :selected_ad_id

-- update a model directives relationship
UPDATE Models_Directives SET ad_id = :ad_id_dropdown WHERE  model_id = :selected_model_id


-- SELECT QUERIES for general data display

-- display aircraft owners
SELECT * FROM Aircraft_Owners ORDER BY owner_name

-- display aircraft models
SELECT * FROM Aircraft_Models ORDER BY model_name

-- display registered aircraft
SELECT aircraft_id, n_number, owner_name, model_name, status FROM Registered_Aircraft 
INNER JOIN Aircraft_Owners ON Aircraft_Owners.owner_id = Registered_Aircraft.owner_id
INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Registered_Aircraft.model_id
GROUP BY n_number ORDER BY n_number

-- display airworthiness directives
SELECT * FROM Airworthiness_Directives ORDER BY ad_number

-- display maintenance records
SELECT maintenance_id,  FROM Maintenance_Records ORDER BY aircraft_id

-- display models/directives relationships grouped and ordered by model
SELECT model_id, model_name, ad_id, ad_number FROM Models_Directives 
INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Models_Directives.model_id
INNER JOIN Airworthiness_Directives ON Airworthiness_Directives.ad_id = Models_Directives.ad_id
GROUP BY model_name ORDER BY model_name

-- display models/directives relationships grouped and ordered by directive
SELECT model_id, model_name, ad_id, ad_number FROM Models_Directives 
INNER JOIN Aircraft_Models ON Aircraft_Models.model_id = Models_Directives.model_id
INNER JOIN Airworthiness_Directives ON Airworthiness_Directives.ad_id = Models_Directives.ad_id
GROUP BY ad_number ORDER BY ad_number


-- SELECT QUERIES for INSERT and UPDATE dropdown menus

-- owner_id dropdown
SELECT owner_id, owner_name FROM Aircraft_Owners ORDER BY owner_name

-- model_id dropdown
SELECT model_id, model_name FROM Aircraft_Models ORDER BY model_name

-- aircraft_id dropdown
SELECT aircraft_id, n_number FROM Registered_Aircraft ORDER BY n_number

--ad_id dropdown
SELECT ad_id, ad_number FROM Airworthiness_Directives ORDER BY ad_number
