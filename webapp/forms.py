from flask_wtf import FlaskForm
from sqlalchemy.orm import defaultload
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DecimalField
from datetime import datetime
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
    active = BooleanField('Usuario activo', validators=[DataRequired()]) #! Boolean
    role = StringField('Rol', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class RegisterEquipo(FlaskForm):
    
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()]) #! Boolean
    DescripcionL = StringField('Descripcion Larga', validators=[DataRequired()])
    DescripcionC = StringField('Descripcion Corta', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    serie = IntegerField('Serie', validators=[DataRequired()])
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    fecha_adquisicion = DateField("Fecha de Adquisición", validators=[DataRequired()], default=datetime.now())
    garantia = StringField('Garantía', validators=[DataRequired()])
    ubicacion = StringField('Ubicación', validators=[DataRequired()])
    mantenimiento = DateField("Mantenimiento", validators=[DataRequired()], default=datetime.now())
    factor_analisis = IntegerField('Factor de Análisis', validators=[DataRequired()])
    medida_factor = IntegerField('Medida Factor', validators=[DataRequired()])
    lim_inferior = IntegerField('Límite Inferior', validators=[DataRequired()])
    lim_superior = IntegerField('Límite Inferior', validators=[DataRequired()])
    especificacion = IntegerField('Límite Inferior', validators=[DataRequired()])
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

class RegisterOrden(FlaskForm):
<<<<<<< HEAD
=======
    
>>>>>>> refs/remotes/origin/main
    cantidad_solicitada = DecimalField('Cantidad Solicitada', validators=[DataRequired()])
    fecha_creada = DateField("Fecha Creada", validators=[DataRequired()], default=datetime.now())
    precio = DecimalField(' Precio', validators=[DataRequired()])
    # idc =  FORANEA
    # certificados = FORANEA

class RegisterLote(FlaskForm):
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/main
    cantidad = DecimalField('Cantidad', validators=[DataRequired()])
    # inspecciones = FORANEA

class RegisterInspeccion(FlaskForm):
<<<<<<< HEAD
=======
   
>>>>>>> refs/remotes/origin/main
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

class RegisteCertificado(FlaskForm):
    cantidad_solicitada = DecimalField('Cantidad Solicitada', validators=[DataRequired()])
    norden = IntegerField('Número de Orden', validators=[DataRequired()])
    cant_total = DecimalField('Cantidad Total', validators=[DataRequired()])
    factura = IntegerField('Factura', validators=[DataRequired()])
    fecha_envio = DateField("Fecha de Envío", validators=[DataRequired()], default=datetime.now())
    fecha_caducidad = DateField("Fecha de Caducidad", validators=[DataRequired()], default=datetime.now())
    # idc = 
    # idl = 
    # norden = 
    # idi = 
