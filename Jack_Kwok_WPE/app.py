from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import uuid
import tkinter as tk
from tkinter import messagebox

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patient-action', methods=['POST'])
def patient_action():
    action = request.form['patient-action']
    if action == 'add':
        return redirect('/addName')
    elif action == 'delete':
        return redirect('/deleteName')
    elif action == 'none':
        return "pick again"

@app.route('/addName', methods=['POST', 'GET'])
def addName():
    error = None
    if request.method == 'POST':
        result = add_valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('addName.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('addName.html', error=error)

@app.route('/deleteName', methods=['POST', 'GET'])
def deleteName():
    error = None
    if request.method == 'GET' :
        # connect to database
        connection = sql.connect('database.db')
        # check if table exists
        try:
            # selects all columns from users table
            cursor = connection.execute('SELECT * FROM users;')
        except sql.OperationalError as e:
            # Display an error message using a popup
            tk.Tk().withdraw()
            messagebox.showerror("Error", "Table not found: " + str(e))
            connection.close()
            return

        # fetch all data
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        # Display the form to the user
        return render_template('deleteName.html', result=result)
    elif request.method == 'POST':
        result = delete_valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('deleteName.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('deleteName.html', error=error)

def add_valid_name(first_name, last_name):
    #connect to database
    connection = sql.connect('database.db')
    # create 'users' table if dne
    connection.execute('CREATE TABLE IF NOT EXISTS users(pid TEXT PRIMARY KEY, firstname TEXT, lastname TEXT);')
    # generate a unique pid
    pid = str(uuid.uuid4().int)
    # insert values into table
    connection.execute('INSERT INTO users (pid, firstname, lastname) VALUES (?,?,?);', (pid, first_name, last_name))
    # commit changes to db
    connection.commit()
    # selects all columns from users table
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()

def delete_valid_name(first_name, last_name):
    # connect to database
    connection = sql.connect('database.db')
    # check if table exists
    try:
        # selects all columns from users table
        cursor = connection.execute('SELECT * FROM users;')
    except sql.OperationalError as e:
        # Display an error message using a popup
        tk.Tk().withdraw()
        messagebox.showerror("Error", "Table not found: " + str(e))
        connection.close()
        return

    # delete entire row values from table
    connection.execute('DELETE FROM users WHERE firstname = ? AND lastname = ?;', (first_name, last_name))
    # commit changes to db
    connection.commit()
    # selects all columns from users table
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()

if __name__ == "__main__":
    app.run()