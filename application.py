
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/variabletest/<name>')
def print_variable(name):
    return 'Hello %s!' % name

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello % as Guest" % guest

@app.route('/user/<user>')
def hello_user(user):
    if user=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=user))


@app.route('/input', methods = ['POST', 'GET'])
def information():
    if request.method == 'POST':
        info = request.form['info']
        return redirect(url_for('hello_guest', guest=info))
    else:
        return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)