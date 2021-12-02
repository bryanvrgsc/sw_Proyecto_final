from typing_extensions import Required
from flask_wtf import FlaskForm
from sqlalchemy.orm import defaultload
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DecimalField, TextAreaField, SelectField, FormField, FieldList
from datetime import datetime
from wtforms.fields.simple import SubmitField
from wtforms.form import Form
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from wtforms.fields.html5 import  TelField, DateField
from wtforms.widgets.html5 import NumberInput
from webapp.models import *


# class RequiredIf(Required):
#     # a validator which makes a field required if
#     # another field is set and has a truthy value

#     def __init__(self, other_field_name, *args, **kwargs):
#         self.other_field_name = other_field_name
#         super(RequiredIf, self).__init__(*args, **kwargs)

#     def __call__(self, form, field):
#         other_field = form._fields.get(self.other_field_name)
#         if other_field is None:
#             raise Exception('no field named "%s" in form' % self.other_field_name)
#         if bool(other_field.data):
#             super(RequiredIf, self).__call__(form, field)



class Login(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Log in')

class Buscar(FlaskForm):
    value = StringField('value')
    search = SubmitField('Buscar')


class RegisterFarinografo(Form):
    absorcion_agua = StringField('Absorcion de Agua')
    tolerancia_ub = StringField('Tolerancia')
    elasticidad = StringField('Elasticidad')
    viscodidad = StringField('Viscodidad')
    act_enzimatica = StringField('Enzimatica')
    trigo_germinado = StringField('Trigo Germinado')
    tiempo_amasado = StringField('Tiempo de Amasado')
    cantidad_gluten = StringField('Cantidad del Gluten')
    calidad_gluten = StringField('Calidad del Gluten')
    indoneidad = StringField('Indoneidad')
    dureza = StringField('Dureza')
    reblandecimiento = StringField('Reblancedimiento') 
    estabilidad = StringField('Estabilidad')
    tiempo_desarrollo = StringField('Tiempo de desarrollo') 
    qnumber = StringField('Qnumber')

class RegisterAlveografo(Form):
    tenacidad = StringField('Tenacidad ')
    extensibilidad = StringField('Extensibilidad')
    fuerza_panadera = StringField('Fuerza Panadera')
    indice_elasticidad = StringField('Índice de Elasticidad')
    configuracion_curva = StringField('Configuración de la Curva')

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
    personalizado_far = BooleanField('Farinografo Personalizado') #! Boolean
    personalizado_alv = BooleanField('Alveografo Personalizado') #! Booleanls

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
    lote = SelectField("Lote", choices=[(table.idlote,table.idlote) for table in Lote.query.all()])
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


    equipo_alv = SelectField("Equipo Utilizado", choices=[(table1.clave, table1.marca) for table1 in EquipoLab.query.filter(EquipoLab.id_alv!="Null").all()])
    equipo_far = SelectField("Equipo Utilizado", choices=[(table2.clave, table2.marca) for table2 in EquipoLab.query.filter(EquipoLab.id_far!= "Null").all()])



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
    inspeccion = SelectField("Inspección", choices=[(table.clave, table.marca) for table in EquipoLab.query.filter(EquipoLab.id_far!= "Null").all()])
    submit = SubmitField('Registrar')

