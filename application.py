
import os
from flask import Flask, redirect, url_for, request, render_template
from forms import RecipeForm
import pandas as pd
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nfjkdhdshkjhfd7864578374nfjsghfi74ujfshj'
app.config['SUBMITTED_DATA'] = os.path.join('static', 'data_dir', '')
app.config['SUBMITTED_IMG'] = os.path.join('static', 'image_dir', '')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add_recipe', methods = ['POST', 'GET'])
def add_recipe():
    if request.method == 'POST':
        rname = request.form['rname']
        print(rname)
        return "Recipe added successfully"
    else:
        return render_template('add_recipe_manual.html')

@app.route('/add_recipe_auto', methods = ['POST', 'GET'])
def add_recipe_auto():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_name = form.recipe_name.data
        ingredients_list = form.ingredients_list.data
        preparation_instructions = form.preparation_instructions.data
        serving_instructions = form.serving_instructions.data
        pic_filename = recipe_name.lower().replace(" ", "_") + '.' + secure_filename(form.recipe_image.data.filename).split('.')[-1]
        form.recipe_image.data.save(os.path.join(app.config['SUBMITTED_IMG'] + pic_filename))
        df = pd.DataFrame([{'Recipe name': recipe_name, 'ingredients': ingredients_list, 'Prep Instructions': preparation_instructions, 'Serving Instructions': serving_instructions, 'image': pic_filename}])
        df.to_csv(os.path.join(app.config['SUBMITTED_DATA'] + recipe_name.lower().replace(" ", "_") + '.csv'))
        print(df)
        return redirect(url_for('hello_world'))
    else:
        return render_template('add_recipe_auto.html', form=form)
@app.route('/display_data/<name>')
def render_information(name):


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