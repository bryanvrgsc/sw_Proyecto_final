from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.core import DecimalField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from wtforms.fields.html5 import  TelField
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
    comfirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    active = BooleanField('Usuario activo', validators=[DataRequired()]) #! Boolean
    role = StringField('Rol', validators=[DataRequired()])
    submit = SubmitField('Registrar')
    
class RegisterCliente(FlaskForm):
    rfc = StringField('RFC', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    domicilio = StringField('Domicilio', validators=[DataRequired()])
    ncontacto = TelField('Numero de contacto', validators=[DataRequired()])
    factor_analisis = DecimalField('Analisis')
    lim_inferior = DecimalField('Limite Inferior')
    lim_superior = DecimalField('Limite Superior')
    clave_factor = DecimalField('Clave Factor')
    medida = DecimalField('Medida')
    submit = SubmitField('Registrar')

class RegiseterEquipo(FlaskForm):
    clave = StringField('Clave', validators=[DataRequired()])
    marca = PasswordField('Marca', validators=[DataRequired()])
    modelo = BooleanField('Modelo', validators=[DataRequired()]) #! Boolean
    DescripcionC = StringField('Descripcion Corta', validators=[DataRequired()])
    submit = SubmitField('Registrar')