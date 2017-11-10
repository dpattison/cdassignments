from flask import Flask, render_template  # Import Flask to allow us to create our app, and import

app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we

@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
def hello_world():
  return render_template('index.html')    # Render the template and return it!


@app.route('/success')
def success():
  return render_template('success.html')

app.run(debug=True)                       # Run the app in debug mode.
