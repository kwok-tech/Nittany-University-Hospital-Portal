# Flask Application for Nittany University Hospital
This is a Flask web application for Nittany University Hospital, where hospital staff can enter and delete patient names in its database. The application is designed using HTML and implemented using Flask.

## Dependencies
The following dependencies are required to run this application:

- Bootstrap
- Flask
- sqlite3
- uuid
- tkinter
## Installation
Clone this repository.
Install the dependencies by running 'pip install -r requirements.txt' in your terminal.
## Usage
Run python app.py in your terminal to start the application.
Open your web browser and navigate to http://127.0.0.1:5000/ to access the homepage.
The user can add or delete patient names by clicking on the respective buttons.
## Code Structure
### app.py
The main file of the Flask application, which contains the routes and logic to add or delete patient names from the database.

### templates
The folder containing HTML templates used by the Flask application.

- index.html: The homepage of the application, containing buttons to add or delete patient names.
- addName.html: The form for adding a patient name to the database.
- deleteName.html: The form for deleting a patient name from the database.
### database.db
The SQLite database file, which contains a patients table to store the added patient names.

### add_valid_name()
A function that adds a patient name to the patients table in the database.

### delete_valid_name()
A function that deletes a patient name from the patients table in the database.

## Pages Description
### Homepage (index.html)
The homepage of the application that displays two buttons: "Add Patient" and "Delete Patient". The index.html file is the landing page of the Nittany University Hospital's patient portal website. It contains a header with the hospital's name and a subtitle indicating that the webpage is for patient portal. The webpage also has a brief description of the webpage's purpose in the form of a text paragraph.

The webpage includes a dropdown menu that allows users to select whether they want to add or delete a patient's name from the hospital's database. The dropdown menu is included in a form that will submit a POST request to the server's "/patient-action" endpoint when the user clicks the "Go!" button.

Flask will be used to implement the functionality of adding and deleting patient names from the hospital's database. The server will handle the POST request sent by the dropdown menu and update the database accordingly. Two more webpages, one for adding a patient's name and one for deleting a patient's name, will be created to complete the functionality of the patient portal website.

### Add Patient Page (addName.html)
This page contains a form that allows the hospital staff to add a patient's first and last name to the patients table in the database. When the user submits the form, it sends a POST request to the server with the patient's name data. The server then adds the patient's name and a uniquely generated pid to the database.

After entering the patient's name and clicking the "Insert" button, the data will be stored in the SQLite database and the page will display the updated patient data history.

### Delete Patient Page (deleteName.html)
This page contains a form that allows the hospital staff to delete a patient's first and last name from the patients table in the database. It displays a table of all the patients' names currently in the database to help the staff identify the patient they want to delete.

This page allows the user to delete a patient's data from the hospital database. The user must enter the patient's first and last name, and then click the "Delete" button. This will open a Bootstrap confirmation modal dialog box, where the user can choose to either delete the patient's data by clicking the "Delete Now" button, or cancel the deletion by clicking the "Close" button.

If the user chooses to delete the patient's data, the page will send a POST request to the server's /deleteName endpoint, which will delete the patient's data from the database. The page will then reload and display the updated list of patients.

The page also displays a table of all the patients currently in the database, with their PID (patient ID), first name, and last name. This table is updated after a deletion has been made. The user can also navigate back to the homepage by clicking the "Go Back" button.