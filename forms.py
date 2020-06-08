from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    email=StringField("Email: ",validators=[DataRequired()])
    password=PasswordField("Password:",validators=[DataRequired()])
    submit=SubmitField()
    
class SignUpForm(FlaskForm):
    email=StringField("Email: ",validators=[DataRequired()])
    password=PasswordField("Password:",validators=[DataRequired()])
    submit=SubmitField()

class ProjectForm(FlaskForm):
    title=StringField("Title: ",validators=[DataRequired()])
    description=StringField("Description: ",validators=[DataRequired()])
    submit=SubmitField()