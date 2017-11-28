from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'emaildb')
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    #check for empty form
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    #check for valid email
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
    #if email is valid, insert into database
    #then redirect to success page
    else:
        query = "INSERT INTO emails (email,created,modified) VALUES (:email,NOW(),NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        flash(request.form['email'])
        return redirect('/success')
    #if not valid, redirect to root page with validation flash message
    return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

app.run(debug=True)
