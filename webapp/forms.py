from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.core import FieldList, FormField
from wtforms.fields.simple import SubmitField
from wtforms.form import Form
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.widgets.html5 import NumberInput

class Login(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Log in')


class Buscar(FlaskForm):
    value = StringField('value')
    submit = SubmitField('Buscar')

class RegiseterLab(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    active = BooleanField('Usuario activo', validators=[DataRequired()]) #! Boolean
    role = StringField('Rol', validators=[DataRequired()])

class RegisterCliente(FlaskForm):
    rfc = StringField('RFC', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    domicilio = StringField('Domicilio', validators=[DataRequired()])
    ncontacto = TelField('Numero de contacto', validators=[DataRequired()])
    factor_analisis = NumberInput('Analisis')
    lim_inferior = NumberInput('Limite Inferior')
    lim_superior = NumberInput('Limite Superior')
    clave_factor = NumberInput('Clave Factor')
    medida = NumberInput('Medida')