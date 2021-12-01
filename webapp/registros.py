from webapp.models import *
from webapp import bcrypt

def regOrden(form):
    orden = Orden(cantidad_solicitada=form.username.data,fecha_creada=form.username.data,precio=form.username.data)

def regFarinografo(form):
    farinografo = Farinografo(absorcion_agua=form.username.data,tolerancia_ub=form.username.data,elasticidad=form.username.data,viscodidad=form.username.data,act_enzimatica=form.username.data,trigo_germinado=form.username.data,tiempo_amasado=form.username.data,cantidad_gluten=form.username.data,calidad_gluten=form.username.data,indoneidad=form.username.data,dureza=form.username.data,reblandecimiento=form.username.data,estabilidad=form.username.data,tiempo_desarrollo=form.username.data,qnumber=form.username.data)

def regAlveografo(form):
    alveografo = Alveografo(tenacidad=form.username.data,extensibilidad=form.username.data,fuerza_panadera=form.username.data,indice_elasticidad=form.username.data,configuracion_curva=form.username.data)

def regLaboratorista(form):
    if form.field.name =="password":
        hashed_password = bcrypt.generate_password_hash(form.field.data).decode('utf-8')
    user = Laboratorista(username=form.username.data, password=hashed_password, role=form.username.data, active=form.username.data)

def regEquipo(form):
    equipo = EquipoLab(marca=form.username.data, modelo=form.username.data, serie=form.username.data, proveedor=form.username.data, fecha_adquisicion=form.username.data, garantia=form.username.data, ubicacion=form.username.data, mantenimiento=form.username.data, descripcionc=form.username.data, descripcionl=form.username.data)

def regCliente(form):
    cliente = Cliente(rfc=form.username.data,nombre=form.username.data,apellido=form.username.data,domicilio=form.username.data,ncontacto=form.username.data,personalizada_far=form.username.data,personalizada_alv=form.username.data)

def regLote(form):
    lote = Lote(cantidad=form.username.data)