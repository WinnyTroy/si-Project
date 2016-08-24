import json


from flask import Flask, render_template, url_for, redirect, make_response, request

app = Flask(__name__)

# json dumps creats json string which is then taken by loads and turned into python code again.
def get_saved_data():
    try:
        data = json.loads(request.cookies.get('cookname'))
    except TypeError:
        data = {}
    return data



@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves = data)



# dict translates key value pairs retrieved from calling .items(), which is then bumped into the jspn by .dumps.
# updates saved data and then sends it back to the user
@app.route('/save', methods = ['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('cookname', json.dumps(data))
    return response


app.run(debug=True, host='0.0.0.0')