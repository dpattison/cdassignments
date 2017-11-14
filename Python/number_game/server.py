from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

target = random.randrange(0, 101)


@app.route('/')
def index():
    session['number'] = target
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    if request.form['guess'] == session['number']:
        return redirect('/')
    else:
        return redirect('/')

# @app.route('/reset', methods=['POST'])
# def reset():
#     session['counter'] = 0
#     return redirect('/')


app.run(debug=True)
