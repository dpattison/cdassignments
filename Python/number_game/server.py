import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'



randnum = random.randrange(0, 101)


@app.route('/')
def index():
    session['randnum'] = randnum
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['randnum']:
        session.pop('randnum')
        session['guess'] = "Correct"
        return redirect('/')
    elif int(request.form['guess']) > session['randnum']:
        session['guess'] = "Too high!"
        return redirect('/')
    elif int(request.form['guess']) < session['randnum']:
        session['guess'] = "Too low!"
        return redirect('/')


app.run(debug=True)
