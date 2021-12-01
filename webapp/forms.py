from flask_wtf import FlaskForm
from sqlalchemy.orm import defaultload
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DecimalField, TextAreaField, SelectField
from datetime import datetime
from wtforms.fields.core import FormField
from wtforms.fields.simple import SubmitField
from wtforms.form import Form
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from wtforms.fields.html5 import  TelField, DateField
from wtforms.widgets.html5 import NumberInput

class Login(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Log in')

class Buscar(Form):
    value = StringField('value')
    search = SubmitField('Buscar')


class RegisterFarinografo(Form):
    absorcion_agua = IntegerField('Absorcion de Agua', validators=[])
    tolerancia_ub = IntegerField('Tolerancia', validators=[])
    elasticidad = IntegerField('Elasticidad', validators=[])
    viscodidad = IntegerField('Viscodidad', validators=[])
    act_enzimatica = IntegerField('Enzimatica', validators=[])
    trigo_germinado = IntegerField('Trigo Germinado', validators=[])
    tiempo_amasado = IntegerField('Tiempo de Amasado', validators=[])
    cantidad_gluten = IntegerField('Cantidad del Gluten', validators=[])
    calidad_gluten = IntegerField('Calidad del Gluten', validators=[])
    indoneidad = IntegerField('Indoneidad', validators=[])
    dureza = IntegerField('Dureza', validators=[])
    reblandecimiento = IntegerField('Reblancedimiento', validators=[]) 
    estabilidad = IntegerField('Estabilidad', validators=[])
    tiempo_desarrollo = IntegerField('Tiempo de desarrollo', validators=[]) 
    qnumber = IntegerField('Qnumber', validators=[])

class RegisterAlveografo(Form):
    tenacidad = IntegerField('Tenacidad ', validators=[])
    extensibilidad = IntegerField('Extensibilidad', validators=[])
    fuerza_panadera = IntegerField('Fuerza Panadera', validators=[])
    indice_elasticidad = IntegerField('Índice de Elasticidad', validators=[])
    configuracion_curva = IntegerField('Configuración de la Curva', validators=[])

class RegiseterLab(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    role = SelectField('Rol', validators=[DataRequired()],choices=[('user', 'Usuario'),('admin', 'Administrador')], default=('user', 'Usuario'))
    active = BooleanField('Usuario activo', validators=[DataRequired()]) #! Boolean
    submit = SubmitField('Registrar')


class RegisterEquipo(FlaskForm):
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    serie = IntegerField('Serie', validators=[DataRequired()])
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    fecha_adquisicion = DateField("Fecha de Adquisición", validators=[DataRequired()], default=datetime.now())
    garantia = DateField("Fecha de Adquisición", validators=[DataRequired()], default=datetime.now())
    ubicacion = StringField('Ubicación', validators=[DataRequired()])
    mantenimiento = DateField("Mantenimiento", validators=[DataRequired()], default=datetime.now())
    descripcionc = StringField('Descripcion Corta', validators=[DataRequired()])
    descripcionl = TextAreaField('Descripcion Larga', validators=[DataRequired(),Length(max=100)])

    alveografo = FormField(RegisterAlveografo)
    farinografo = FormField(RegisterFarinografo)

    submit = SubmitField('Registrar')


    
class RegisterCliente(FlaskForm):
    rfc = StringField('RFC', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    domicilio = StringField('Domicilio', validators=[DataRequired()])
    ncontacto = TelField('Número de contacto', validators=[DataRequired()])
    n_orden = SelectField("Número de Orden", validators=[DataRequired()])
    personalizado_far = BooleanField('Farinografo Personalizado', validators=[DataRequired()]) #! Boolean
    personalizado_alv = BooleanField('Alveografo Personalizado', validators=[DataRequired()]) #! Boolean

    alveografo = FormField(RegisterAlveografo)
    farinografo = FormField(RegisterFarinografo)

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
    id_inspeccion = StringField("ID de Inspeccion", validators=[DataRequired()])
    absorcion = DecimalField('Absorción', validators=[DataRequired()])
    tiempo_desarrollo = DecimalField('Tiempo Desarrollo', validators=[DataRequired()])
    estabilidad = DecimalField('Estabilidad', validators=[DataRequired()])
    reblandecimiento = DecimalField('Reblandecimiento', validators=[DataRequired()])
    qnumber = IntegerField('Numero de Calidad', validators=[DataRequired()])
    tenacidad = DecimalField('Tenacidad', validators=[DataRequired()])
    extensibilidad = DecimalField('Extensibilidad', validators=[DataRequired()])
    configuracion_curva = DecimalField('Configuración Curva', validators=[DataRequired()])
    indice_elasticidad = DecimalField('Índice Elasticidad', validators=[DataRequired()])
    fuerza_panadera = DecimalField('Fuerza Panadera', validators=[DataRequired()])
    lote = SelectField("Lote")

    equipo_alv = SelectField("Equipo Utilizado")
    equipo_far = SelectField("Equipo Utilizado")



    alveografo = FormField(RegisterAlveografo)
    farinografo = FormField(RegisterFarinografo)


    # certificados = FORANEA
    submit = SubmitField('Registrar')

class RegisterCertificado(FlaskForm):
    cantidad_solicitada = DecimalField('Cantidad Solicitada', validators=[DataRequired()])
    cant_total = DecimalField('Cantidad Total', validators=[DataRequired()])
    factura = IntegerField('Factura', validators=[DataRequired()])
    fecha_envio = DateField("Fecha de Envío", validators=[DataRequired()], default=datetime.now())
    fecha_caducidad = DateField("Fecha de Caducidad", validators=[DataRequired()], default=datetime.now())
    inspeccion = SelectField("Inspección")
    submit = SubmitField('Registrar')

