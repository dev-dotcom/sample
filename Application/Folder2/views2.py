from Application import app
from flask import render_template

@app.route('/views2')
def sample2():
    return render_template('sample2.html')