import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'






@app.route('/')
def index():
    session['randnum']= random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['randnum']:
        session.pop('randnum')
        answer = "Correct"
        
    elif int(request.form['guess']) > session['randnum']:
        answer = "Too high!"
        
    elif int(request.form['guess']) < session['randnum']:
        answer = "Too low!"

    return render_template('index.html', answer=answer)


app.run(debug=True)
