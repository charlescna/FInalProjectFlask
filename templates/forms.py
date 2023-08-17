
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe_Name:', validators=[DataRequired()])
    ingredients_list = TextAreaField('List of Ingredients:', validators=[DataRequired(), Length(200)])
    preparation_instructions = TextAreaField('Preparation Instructions:', validators=[DataRequired(), Length(300)])
    serving_instructions = TextAreaField('Serving Instructions:', validators=[DataRequired(), Length(100)])
    recipe_image = FileField('Image of Recipe:', validators=[FileRequired()])