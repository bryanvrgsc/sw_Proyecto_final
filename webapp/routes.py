from re import search
import re
from flask import render_template, request, redirect, session, url_for, flash, Markup
from webapp import app, db, bcrypt
from webapp.forms import  *
from webapp.models import *
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from datetime import datetime
from sqlalchemy.inspection import inspect

def TableValues(elemento):

    if elemento == "laboratorista" and current_user.role == 'admin':
        return {'model' : Laboratorista(), 'search_item' : 'username', 'table_header' : Laboratorista.__table__.columns.keys()}
    elif elemento == "clientes":
        return {'model' : Cliente(), 'search_item' : 'rfc', 'table_header' : Cliente.__table__.columns.keys() }
    elif elemento == "equipo":
        return {'model' : EquipoLab(),'search_item' : 'clave', 'table_header' : EquipoLab.__table__.columns.keys() }
    elif elemento == "certificados":
        return {'model' : Certificado, 'search_item' : 'ncertificado', 'table_header' : Certificado.__table__.columns.keys() }
    elif elemento == "registro":
        return {'model' : Inspeccion(),' search_item' : 'idi', 'table_header' : Inspeccion.__table__.columns.keys() }
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
    modalForm = {
            'laboratorista' : RegiseterLab(),
            'clientes' : RegisterCliente(),
            'equipo': RegiseterEquipo()
    }

    # Agregar Valor a la base de datos
    if modalForm[elemento].validate_on_submit():
        flash("Se envio el fomrulario", "info")
    
    print(search_form.validate_on_submit())

    # Filtar con busqueda
    table = TableValues(elemento)
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
    table_header=table['table_header'], 
    search_item = table['search_item'].upper(),
    # Formularios a usar
    form=search_form, 
    modalForm=modalForm[elemento])



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
    flash(f"El conepto con ID: {value_id} fue eliminado ", 'warning')

    return redirect(url_for('buscador', elemento=elemento))


@app.route("/seleccionar/<elemento>/<value_id>")
@login_required
def seleccionar(elemento,value_id):

    return redirect(url_for('buscador', elemento=elemento))

# Creacion de certificado
@app.route("/creacion-certificado")
def creacion_certificado():
    if current_user.is_authenticated:
        pass
