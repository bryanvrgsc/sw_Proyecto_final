from re import search
import re
from flask import render_template, request, redirect, session, url_for, flash, Markup, Response
from webapp import app, db, bcrypt, APP_ROOT, Download_PATH, Download_FOLDER
from webapp.forms import  *
from webapp.models import *
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from datetime import datetime
from sqlalchemy.inspection import inspect
import pdfkit, os, uuid

def getLastId(Table):
    obj = Table().query.all()
    return obj[-1]


def regOrden(form):
    orden = Orden(cantidad_solicitada=form.cantidad_solicitada.data, fecha_creada=form.fecha_creada.data, precio=form.precio.data)
    return orden

def regFarinografo(form):
    farinografo = Farinografo(absorcion_agua=form.absorcion_agua.data, tolerancia_ub=form.tolerancia_ub.data, elasticidad=form.elasticidad.data, viscodidad=form.viscodidad.data, act_enzimatica=form.act_enzimatica.data, trigo_germinado=form.trigo_germinado.data, tiempo_amasado=form.tiempo_amasado.data, cantidad_gluten=form.cantidad_gluten.data, calidad_gluten=form.calidad_gluten.data, indoneidad=form.indoneidad.data, dureza=form.dureza.data, reblandecimiento=form.reblandecimiento.data, estabilidad=form.estabilidad.data, tiempo_desarrollo=form.tiempo_desarrollo.data,qnumber=form.qnumber.data)
    return farinografo

def regAlveografo(form):
    alveografo = Alveografo(tenacidad=form.tenacidad.data, extensibilidad=form.extensibilidad.data, fuerza_panadera=form.fuerza_panadera.data, indice_elasticidad=form.indice_elasticidad.data, configuracion_curva=form.configuracion_curva.data) 
    return alveografo

def regLaboratorista(form):
    if form.password.name =="password":
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = Laboratorista(username=form.username.data, password=hashed_password, role=form.role.data, active=form.active.data)
    db.session.add(user)
    db.session.commit()
    return{"message": f"El usuario {user.username} ha sido registrado con exito" , "type": "success"}

def regEquipo(form):
    equipo = EquipoLab(marca=form.marca.data, modelo=form.modelo.data, serie=form.serie.data, proveedor=form.proveedor.data, fecha_adquisicion=form.fecha_adquisicion.data, garantia=form.garantia.data, ubicacion=form.ubicacion.data, mantenimiento=form.mantenimiento.data, descripcionc=form.descripcionc.data, descripcionl=form.descripcionl.data)


    if form.tipo.data == "alv":
        alveografo = regAlveografo(form.alveografo)
        db.session.add(alveografo)
        new_alv_id = str(getLastId(Alveografo).id_alv)
        equipo.id_alv = new_alv_id
    elif form.tipo.data == "far":
        farinografo = regFarinografo(form.farinografo)
        db.session.add(farinografo)
        new_far_id =  str(getLastId(Farinografo).id_far)
        equipo.id_far = new_far_id

    db.session.add(equipo)
    db.session.commit()
    return{"message": f"El equipo {equipo.marca} ha sido registrado con exito" , "type": "success"}
    
def regCliente(form):
    cliente = Cliente(rfc=form.rfc.data, nombre=form.nombre.data, apellido=form.apellido.data, domicilio=form.domicilio.data, ncontacto=form.ncontacto.data, personalizado_far=form.personalizado_far.data, personalizado_alv=form.personalizado_alv.data)

    if cliente.personalizado_alv == True:
        alveografo = regAlveografo(form.alveografo)
        db.session.add(alveografo)
        new_alv_id = str(getLastId(Alveografo).id_alv)
        cliente.id_alv = new_alv_id


    if cliente.personalizado_far == True:
        farinografo = regFarinografo(form.farinografo)
        db.session.add(farinografo)
        new_far_id =  str(getLastId(Farinografo).id_far)
        cliente.id_far = new_far_id

    db.session.add(cliente)
    db.session.commit()

    return{"message": f"{cliente.nombre} ha sido registrado con exito" , "type": "success"}

def regLote(form):
    lote = Lote(cantidad=form.cantidad.data) 
    return lote

def regInspeccion(form):
    # Registro de campos basicos en inspeccion
    inspeccion = Inspeccion(id_inspeccion=form.id_inspeccion.data, clave_alv=form.equipo_alv.data, clave_far=form.equipo_far.data)

    # creacion de alveofrafo y farinografo nuevo
    alveografo = regAlveografo(form.alveografo)
    db.session.add(alveografo)
    new_alv_id = str(getLastId(Alveografo).id_alv)
    inspeccion.id_alv = new_alv_id
    farinografo = regFarinografo(form.farinografo)
    db.session.add(farinografo)
    new_far_id =  str(getLastId(Farinografo).id_far)
    inspeccion.id_far = new_far_id

    
    # asignacion del campo lote
    if form.loteSelect:
        # select:  Se selecciona el campo de select en el formulario y se guarda en la base
        inspeccion.idlote = form.loteSelect.data
    else:
        # Formulario: Se crea un nuevo lote y se adquire su id para agregarlo a la base
        flash(f"La creacion del lote se creo con exito" , "info")

    db.session.add(inspeccion)
    db.session.commit()


    return{"message": f"{inspeccion.id_inspeccion} ha sido registrada con exito" , "type": "success"}


def regCertificado(form):
    for value in form:
        print(value)


def TableValues(elemento):

    if elemento == "laboratorista":
        return {'uncalled': Laboratorista,'model' : Laboratorista(), 'search_item' : 'username', 'table_header' : Laboratorista.__table__.columns.keys(), 'breakpoint': None, 'registro': regLaboratorista}
    elif elemento == "clientes":
        return {'uncalled': Cliente,'model' : Cliente(), 'search_item' : 'rfc', 'table_header' : Cliente.__table__.columns.keys() , 'breakpoint': 'personalizado_far', 'registro': regCliente}
    elif elemento == "equipo":
        return {'uncalled': EquipoLab,'model' : EquipoLab(),'search_item' : 'clave', 'table_header' : EquipoLab.__table__.columns.keys() , 'breakpoint': 'descripcionl', 'registro': regEquipo}
    elif elemento == "certificados":
        return {'uncalled': Certificado,'model' : Certificado(), 'search_item' : 'ncertificado', 'table_header' : Certificado.__table__.columns.keys() , 'breakpoint': 'idl', 'registro': regCertificado}
    elif elemento == "inspeccion":
        return {'uncalled': Inspeccion,'model' : Inspeccion(),'search_item' : 'idi', 'table_header' : Inspeccion.__table__.columns.keys() , 'breakpoint': None, 'registro': regInspeccion}
    else:
        return {'error message' : 'Query Invalido', 'type':'alert'}


@app.route("/", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('menu'))
        
    form = Login()
    if form.validate_on_submit():
        user = Laboratorista.query.filter_by(username= form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('menu'))
            else:
                flash("Contraseña Incorrecta.","danger")
        else:
            flash("Login invalido, Revisa tus credenciales","danger")

    return render_template("login.html", form=form)


@app.route("/menu", methods=["GET","POST"])
@login_required
def menu():    
    user_type = current_user.role
    return render_template("menu.html", user_type=user_type, menu_items=menu)

@app.route("/buscador/<elemento>", methods=["GET", "POST"])
@login_required
def buscador(elemento):
    search_form = Buscar()

    # Largo de Table Header
    table = TableValues(elemento)

    table_header = table['table_header']
    if table['breakpoint']:
        index = table_header.index(table['breakpoint'])
        table_header = table_header[0:index]

    # Filtar con busqueda
   
    if search_form.validate_on_submit():
        kwargs = {table['search_item']: search_form.value.data}    
        table_items = table['model'].query.filter_by(**kwargs)
    else:
        table_items = table['model'].query.all()

    
    if 'error message' in table:
        flash(table['error message'], table['type'])
        return redirect(url_for('menu'))
    
    return render_template("buscador.html", 
    elemento=str(elemento).capitalize(), 
    table_items=table_items, 
    table_header=table_header, 
    search_item = table['search_item'].upper(),
    # Formularios a usar
    form=search_form)

@app.route("/register/<elemento>",methods=["GET", "POST"], defaults={'l_nuevo': None} )
@app.route("/register/<elemento>/<l_nuevo>",methods=["GET", "POST"])
# @login_required
def formulario(elemento, l_nuevo):
    elemento = elemento.lower()
    modalForm = {
        'laboratorista' : RegiseterLab(),
        'clientes' : RegisterCliente(),
        'equipo': RegisterEquipo(),
        'certificados': RegisterCertificado(),
        'inspeccion': RegisterInspeccionNo()
    }
    if l_nuevo == "si":
        modalForm["inspeccion"] = RegisterInspeccionSi()

    if modalForm[elemento].validate_on_submit():
        table = TableValues(elemento)        
        message = table['registro'](modalForm[elemento])
        flash(message['message'], message["type"])

    return render_template(f"formularios/{elemento}.html", elemento=elemento, form=modalForm[elemento], l_nuevo=l_nuevo)


# Log Out
@app.route("/logout")
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('login'))


# Acciones de tabla

# ELIMINAR REGISTRO
@app.route("/eliminar/<elemento>/<value_id>")
# @login_required
def eliminar(elemento,value_id):
    
    elemento = str(elemento).lower()
    table = TableValues(elemento)['model']
    result = table.query.get(value_id)
    db.session.delete(result)
    db.session.commit()
    # flash(f'{elemento, value_id}','info')
    flash(f"El coneptxo con ID: {value_id} fue eliminado ", 'warning')

    return redirect(url_for('buscador', elemento=elemento))

@app.route("/seleccionar/<elemento>/<value_id>")
# @login_required 
def seleccionar(elemento,value_id):
    elemento = str(elemento).lower()
    tabla = TableValues(elemento)
    value = tabla['model'].query.get(value_id)
    print(value)
    return render_template(f"info_templates/{elemento}.html",
     value=value,
     table_header=tabla["table_header"])
    # render_template('pdf_templates/certificado.html', value=value)


''' -------------------------------------------------
wkhtmltopdf pdf creator
 -------------------------------------------------'''

@app.route("/api/createPDF/<elemento>/<value_id>")
@login_required
def creacion_certificado(elemento,value_id):
    table = TableValues(str(elemento).lower())
    kwargs = {table['table_header'][0]: value_id}
    value = table['model'].query.filter_by(**kwargs).one()
    template = render_template('pdf_templates/certificado.html', value=value)
    
    try:
        filename = str(uuid.uuid4()) + '.pdf'
        config = pdfkit.configuration(wkhtmltopdf=Download_FOLDER)
        pdfkit.from_string(template, filename, configuration=config)
        pdfDownload = open(filename, 'rb').read()
        os.remove(filename)
        return Response(
            pdfDownload,
            mimetype="application/pdf",
            headers={
                "Content-disposition": "attachment; filename=" + filename,
                "Content-type": "application/force-download"
            }
        )
    except ValueError:
        print("Oops! ")


# Ruta para editar el template de de los certificados para el pdf
# @app.route("/edicion-template/<value_id>")
# def edicion_template(value_id):
#     tabla = TableValues('certificados')

#     value = tabla['model'].query.get(value_id)

#     return render_template('pdf_templates/certificado.html', value=value)