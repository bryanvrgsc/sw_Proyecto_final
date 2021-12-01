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

def TableValues(elemento):

    if elemento == "laboratorista":
        return {'uncalled': Laboratorista,'model' : Laboratorista(), 'search_item' : 'username', 'table_header' : Laboratorista.__table__.columns.keys(), 'breakpoint': None}
    elif elemento == "clientes":
        return {'uncalled': Cliente,'model' : Cliente(), 'search_item' : 'rfc', 'table_header' : Cliente.__table__.columns.keys() , 'breakpoint': 'personalizado_far'}
    elif elemento == "equipo":
        return {'uncalled': EquipoLab,'model' : EquipoLab(),'search_item' : 'clave', 'table_header' : EquipoLab.__table__.columns.keys() , 'breakpoint': 'DescripcionL'}
    elif elemento == "certificados":
        return {'uncalled': Certificado,'model' : Certificado(), 'search_item' : 'ncertificado', 'table_header' : Certificado.__table__.columns.keys() , 'breakpoint': 'idc'}
    elif elemento == "inspeccion":
        return {'uncalled': Inspeccion,'model' : Inspeccion(),'search_item' : 'idi', 'table_header' : Inspeccion.__table__.columns.keys() , 'breakpoint': None}
    else:
        return {'error message' : 'Query Invalido', 'type':'alert'}


@app.route("/login", methods=["GET","POST"])
def login():
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

@app.route("/home", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
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

@app.route("/register/<elemento>", methods=["GET", "POST"])
# @login_required
def formulario(elemento):
    elemento = elemento.lower()
    modalForm = {
        'laboratorista' : RegiseterLab(),
        'clientes' : RegisterCliente(),
        'equipo': RegisterEquipo(),
        'certificados': RegisterCertificado(),
        'inspeccion': RegisterInspeccion()
    }
    if modalForm[elemento].validate_on_submit():
        flash("Funciona", "info")

        table = TableValues(elemento)
        
        object_items = dict()

        for field in modalForm[elemento]:
            if field.widget.input_type != 'hidden' and field.widget.input_type != 'submit':
                if field.name != 'comfirm_password':
                    if elemento == 'laboratorista' and field.name =="password":
                        hashed_password = bcrypt.generate_password_hash(field.data).decode('utf-8')
                        object_items[field.name] = hashed_password
                    else:
                        object_items[field.name] =  field.data
                    
        print(object_items)
        doc = table['uncalled'](**object_items)
        db.session.add(doc)
        db.session.commit()

    return render_template("formulario.html", elemento=elemento, modalForm=modalForm[elemento])


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
@login_required
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
@login_required
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