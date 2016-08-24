import json


from flask import Flask, render_template, url_for, redirect, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods = ['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('cookname', json.dumps(dict(request.form.items())))
    return response


app.run(debug=True, host='0.0.0.0')