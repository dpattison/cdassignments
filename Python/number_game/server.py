from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random

randnum = random.randrange(0,101)

@app.route('/')
def index():
    session['randnum'] = randnum
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    return redirect('/')

# @app.route('/reset', methods=['POST'])
# def reset():
#     session['counter'] = 0
#     return redirect('/')

app.run(debug=True)
