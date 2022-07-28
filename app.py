# This is the flask application used to create the frontend of the website for adding the doctor records
# I am still working on creating the input into the database.

# Upto now, i have got the server running and able to display the frontend of the webpage that is being created 
# temporarily

from flask import Flask,render_template,request

import sqlite3 as sql

# had to specify the template_folder='template' option into the code block
# since i was facing an error in display the html content
# folder had to be renamed to template
app = Flask(__name__, template_folder='template')

# Homepage for the website
@app.route('/')
def home():
    return render_template('home.html')

# Adding more routes

# routes for entering data into the doctor table
@app.route('/enternew')
def new_doctor():
    return render_template('doctor.html')


if __name__ == '__main__':
    app.run(debug=True)

