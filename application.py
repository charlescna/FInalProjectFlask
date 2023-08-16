
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add_recipe')
def add_recipe():
    return render_template('index.html')


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

@app.route('/templatesample')
def table_example():
    username = 'Micahel'
    avg_score = 70
    marks_dict = {'phy': 50, 'che': 70, 'math': 50}
    return render_template('templatesample.html', name=username, marks = avg_score, results = marks_dict)

if __name__ == '__main__':
    app.run(debug=True)