
-- Create Aircraft_Owners table and populate with example data
CREATE TABLE Aircraft_Owners (
    owner_id int NOT NULL UNIQUE AUTO_INCREMENT,
    owner_name varchar(50) UNIQUE NOT NULL,
    owner_email varchar(50) NOT NULL,
    PRIMARY KEY (owner_id)
);

INSERT INTO Aircraft_Owners (

    owner_name,
    owner_email

)
VALUES
(
    "Josh Embury",
    "emburyj@oregonstate.edu"
),
(
    "Ian Bubier",
    "bubieri@oregonstate.edu"
),
(
    "United Airlines",
    "therealunited@aol.com"
),
(
    "Alaska Airlines",
    "alaskaair@hotmail.com"
);

-- Create Aircraft_Models table and populate with example data
CREATE TABLE Aircraft_Models (
    model_id int NOT NULL UNIQUE AUTO_INCREMENT,
    manufacturer_name varchar(50) NOT NULL,
    model_name varchar(50) UNIQUE NOT NULL,
    PRIMARY KEY (model_id)
);

INSERT INTO Aircraft_Models (

    manufacturer_name,
    model_name
)

VALUES
(
    "The Boeing Company",
    "737-8"
),
(
    "The Boeing Company",
    "737-9"
),
(
    "Airbus SAS",
    "A320-214"
),
(
    "Epic Aircraft",
    "E1000"
);

-- Create Registered_Aircraft table and populate with example data
CREATE TABLE Registered_Aircraft (
    aircraft_id int NOT NULL UNIQUE AUTO_INCREMENT,
    n_number varchar(50) UNIQUE NOT NULL,
    owner_id int,
    model_id int,
    status varchar(50) NOT NULL,
    PRIMARY KEY (aircraft_id),
    FOREIGN KEY (owner_id) REFERENCES Aircraft_Owners (owner_id),
    FOREIGN KEY (model_id) REFERENCES Aircraft_Models (model_id)
);

INSERT INTO Registered_Aircraft (

    n_number,
    owner_id,
    model_id,
    status
)

VALUES
(
    "N921AK",
    (SELECT owner_id FROM Aircraft_Owners WHERE owner_name = "Josh Embury"),
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "737-9"),
    "Grounded for Maintenance"
),
(
    "N200MR",
    (SELECT owner_id FROM Aircraft_Owners WHERE owner_name = "Ian Bubier"),
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "E1000"),
    "In-Service"
),
(
    "N291BT",
    (SELECT owner_id FROM Aircraft_Owners WHERE owner_name = "Alaska Airlines"),
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "737-9"),
    "Pending Maintenance"
);

-- Create Airworthiness_Directives table and populate with example data
CREATE TABLE Airworthiness_Directives (
    ad_id int NOT NULL UNIQUE AUTO_INCREMENT,
    ad_number varchar(50) UNIQUE NOT NULL,
    ad_description varchar(511),
    maintenance_required_date date NOT NULL,
    PRIMARY KEY (ad_id)
);

INSERT INTO Airworthiness_Directives (
    ad_number,
    ad_description,
    maintenance_required_date
)
VALUES
(
    "2024-06-03",
    " The loss of the SPCU and ground through the P6 panel could result
     in the loss of significant flightcrew instrumentation and displays.
      This AD requires installing two bonding jumpers from the P6 panel
       structure to primary structure.",
    "2024-05-02"
),
(
    "2024-02-51_Emergency",
    "This emergency AD was prompted by a report of an in-flight departure
    of a mid cabin door plug, which resulted in a rapid decompression of
     the airplane. The FAA is issuing this AD to address the potential
    in-flight loss of a mid cabin door plug, which could result in injury
    to passengers and crew, the door impacting the airplane, and/or loss
    of control of the airplane.",
    "2024-01-06"
),
(
    "2024-06-07",
    "To address incomplete installations of the over wing panel lug attachments
     in the production assembly line, which, if not detected and corrected, could
      reduce the structural integrity of the wing.",
    "2024-05-22"
);

-- Create Maintenance_Records table and populate with example data
CREATE Table Maintenance_Records (
    maintenance_id int NOT NULL UNIQUE AUTO_INCREMENT,
    aircraft_id int,
    maintenance_date date NOT NULL,
    PRIMARY KEY (maintenance_id),
    FOREIGN KEY (aircraft_id) REFERENCES Registered_Aircraft(aircraft_id)
);

INSERT INTO Maintenance_Records (
    aircraft_id,
    maintenance_date
)

VALUES
(
    (SELECT aircraft_id FROM Registered_Aircraft WHERE n_number = "N921AK"),
    "2018-10-30"
),
(
    (SELECT aircraft_id FROM Registered_Aircraft WHERE n_number = "N921AK"),
    "2019-01-15"
),
(
    (SELECT aircraft_id FROM Registered_Aircraft WHERE n_number = "N921AK"),
    "2021-06-18"
),
(
    (SELECT aircraft_id FROM Registered_Aircraft WHERE n_number = "N200MR"),
    "2023-07-29"
),
(
    (SELECT aircraft_id FROM Registered_Aircraft WHERE n_number = "N291BT"),
    "2024-01-05"
);

-- Create Models_Directives table and populate with example data
CREATE TABLE Models_Directives (
    md_id int NOT NULL UNIQUE AUTO_INCREMENT,
    model_id int,
    ad_id int,
    PRIMARY KEY (md_id),
    FOREIGN KEY (model_id) REFERENCES Aircraft_Models(model_id),
    FOREIGN KEY (ad_id) REFERENCES Airworthiness_Directives(ad_id)
);

INSERT INTO Models_Directives (
    model_id,
    ad_id
)

VALUES
(
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "737-9"),
    (SELECT ad_id FROM Airworthiness_Directives WHERE ad_number = "2024-02-51_Emergency")
),
(
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "737-8"),
    (SELECT ad_id FROM Airworthiness_Directives WHERE ad_number = "2024-06-03")
),
(
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "737-9"),
    (SELECT ad_id FROM Airworthiness_Directives WHERE ad_number = "2024-06-03")
),
(
    (SELECT model_id FROM Aircraft_Models WHERE model_name = "A320-214"),
    (SELECT ad_id FROM Airworthiness_Directives WHERE ad_number = "2024-06-07")
);