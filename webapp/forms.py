from flask_wtf import FlaskForm
from sqlalchemy.orm import defaultload
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DecimalField, TextAreaField
from datetime import datetime
from wtforms.fields.core import SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from wtforms.fields.html5 import  TelField, DateField
from wtforms.widgets.html5 import NumberInput

class Login(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Log in')


class Buscar(FlaskForm):
    value = StringField('value')
    search = SubmitField('Buscar')

class RegiseterLab(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    comfirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    role = SelectField('Rol', validators=[DataRequired()],choices=[('user', 'Usuario'),('admin', 'Administrador')], default=('user', 'Usuario'))
    active = BooleanField('Usuario activo', validators=[DataRequired()]) #! Boolean
    submit = SubmitField('Registrar')


class RegisterEquipo(FlaskForm):
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    DescripcionL = TextAreaField('Descripcion Larga', validators=[DataRequired(), Length(max=100)])
    DescripcionC = StringField('Descripcion Corta', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    serie = IntegerField('Serie', validators=[DataRequired()])
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    fecha_adquisicion = DateField("Fecha de Adquisición", validators=[DataRequired()], default=datetime.now())
    garantia = StringField('Garantía', validators=[DataRequired()])
    ubicacion = StringField('Ubicación', validators=[DataRequired()])
    mantenimiento = DateField("Mantenimiento", validators=[DataRequired()], default=datetime.now())
    descripcionc = StringField('Descripcion Corta', validators=[DataRequired()])
    descripcionl = TextAreaField('Descripcion Larga', validators=[DataRequired(),Length(max=100)])

    submit = SubmitField('Registrar')

class RegisterFarinografo(FlaskForm):
    absorcion_agua = IntegerField('Absorcion de Agua', validators=[DataRequired()])
    tolerancia_ub = IntegerField('Tolerancia', validators=[DataRequired()])
    elasticidad = IntegerField('Elasticidad', validators=[DataRequired()])
    viscodidad = IntegerField('Viscodidad', validators=[DataRequired()])
    act_enzimatica = IntegerField('Enzimatica', validators=[DataRequired()])
    trigo_germinado = IntegerField('Trigo Germinado', validators=[DataRequired()])
    tiempo_amasado = IntegerField('Tiempo de Amasado', validators=[DataRequired()])
    cantidad_gluten = IntegerField('Cantidad del Gluten', validators=[DataRequired()])
    calidad_gluten = IntegerField('Calidad del Gluten', validators=[DataRequired()])
    indoneidad = IntegerField('Indoneidad', validators=[DataRequired()])
    dureza = IntegerField('Dureza', validators=[DataRequired()])
    reblandecimiento = IntegerField('Reblancedimiento', validators=[DataRequired()]) 
    estabilidad = IntegerField('Estabilidad', validators=[DataRequired()])
    tiempo_desarrollo = IntegerField('Tiempo de desarrollo', validators=[DataRequired()]) 
    qnumber = IntegerField('Qnumber', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class RegisterAlveografo(FlaskForm):
    tenacidad = IntegerField('Tenacidad ', validators=[DataRequired()])
    extensibilidad = IntegerField('Extensibilidad', validators=[DataRequired()])
    fuerza_panadera = IntegerField('Fuerza Panadera', validators=[DataRequired()])
    indice_elasticidad = IntegerField('Índice de Elasticidad', validators=[DataRequired()])
    configuracion_curva = IntegerField('Configuración de la Curva', validators=[DataRequired()])
    
class RegisterCliente(FlaskForm):
    rfc = StringField('RFC', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    domicilio = StringField('Domicilio', validators=[DataRequired()])
    ncontacto = TelField('Número de contacto', validators=[DataRequired()])
    personalizado_far = BooleanField('Farinografo Personalizado', validators=[DataRequired()]) #! Boolean
    personalizado_alv = BooleanField('Alveografo Personalizado', validators=[DataRequired()]) #! Boolean
    submit = SubmitField('Registrar')

class RegisterOrden(FlaskForm):

    cantidad_solicitada = DecimalField('Cantidad Solicitada', validators=[DataRequired()])
    fecha_creada = DateField("Fecha Creada", validators=[DataRequired()], default=datetime.now())
    precio = DecimalField(' Precio', validators=[DataRequired()])
    # idc =  FORANEA
    # certificados = FORANEA
    submit = SubmitField('Registrar')

class RegisterLote(FlaskForm):

    cantidad = DecimalField('Cantidad', validators=[DataRequired()])
    # inspecciones = FORANEA
    submit = SubmitField('Registrar')

class RegisterInspeccion(FlaskForm):
    absorcion = DecimalField('Absorción', validators=[DataRequired()])
    tiempo_desarrollo = DecimalField('Tiempo Desarrollo', validators=[DataRequired()])
    estabilidad = DecimalField('Estabilidad', validators=[DataRequired()])
    reblandecimiento = DecimalField('Reblandecimiento', validators=[DataRequired()])
    qnumber = IntegerField('QNumber', validators=[DataRequired()])
    tenacidad = DecimalField('Tenacidad', validators=[DataRequired()])
    extensibilidad = DecimalField('Extensibilidad', validators=[DataRequired()])
    configuracion_curva = DecimalField('Configuración Curva', validators=[DataRequired()])
    indice_elasticidad = DecimalField('Índice Elasticidad', validators=[DataRequired()])
    fuerza_panadera = DecimalField('Fuerza Panadera', validators=[DataRequired()])

    # certificados = FORANEA
    # idLote = FORANEA
    submit = SubmitField('Registrar')

class RegisterCertificado(FlaskForm):
    cantidad_solicitada = DecimalField('Cantidad Solicitada', validators=[DataRequired()])
    cant_total = DecimalField('Cantidad Total', validators=[DataRequired()])
    factura = IntegerField('Factura', validators=[DataRequired()])
    fecha_envio = DateField("Fecha de Envío", validators=[DataRequired()], default=datetime.now())
    fecha_caducidad = DateField("Fecha de Caducidad", validators=[DataRequired()], default=datetime.now())
    # idc = 
    # idl = 
    # norden = 
    # idi = 
    submit = SubmitField('Registrar')

