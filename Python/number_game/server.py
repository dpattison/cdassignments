<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, session
import random
=======
import random
from flask import Flask, render_template, request, redirect, session
>>>>>>> d2e4d0b1b63c6bca9248952c9ff4289ba2582393

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

<<<<<<< HEAD
target = random.randrange(0, 101)
=======



>>>>>>> d2e4d0b1b63c6bca9248952c9ff4289ba2582393


@app.route('/')
def index():
<<<<<<< HEAD
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
=======
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
>>>>>>> d2e4d0b1b63c6bca9248952c9ff4289ba2582393


app.run(debug=True)
