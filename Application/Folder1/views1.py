from Application import app
from flask import render_template

@app.route('/views1')
def sample1():
    return render_template('sample1.html')