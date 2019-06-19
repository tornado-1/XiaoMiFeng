# coding=utf-8
from flask_wtf import FlaskForm,Form
from wtforms import StringField,TextAreaField,IntegerField,FloatField,DateTimeField,SelectField
from wtforms.validators import DataRequired,Length

class calProblemForm(FlaskForm):
    subAns=IntegerField(
        'subAns'
    )





class LoginForm(Form):
    name=StringField(
        'login_name',
        validators=[DataRequired(),Length(max=20)]
    )
    password=StringField(
        'password',
        validators=[DataRequired(),Length(max=20)]
                         )
