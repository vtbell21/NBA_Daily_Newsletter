from flask import Flask, render_template, request, redirect, url_for
import pyodbc
import os
from dotenv import load_dotenv

app = Flask(__name__, static_folder='styles')

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE')

# connect to the database
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

# Define a route for the landing page


@app.route('/')
def landing_page():
    return render_template('index.html')

# Define a route for handling form submissions


@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO emails (email_address) VALUES (?)", email)
    cursor.commit()
    return redirect(url_for('thankyou'))


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
