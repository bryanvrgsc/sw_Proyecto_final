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

# Formatear Imagen para guardarse
def save_file(form_file, folder_name):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_file.filename)
    file_name = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static" , folder_name, file_name)

    # Delete Existing File
    if current_user.is_authenticated:
        if folder_name == "HeadShots":
            if current_user.picture != "default-profile.jpg":
                os.remove(os.path.join(app.root_path, "static" , folder_name, current_user.picture))
        if folder_name == "b_certificate":
            if current_user.b_certificate != None:
                os.remove(os.path.join(app.root_path, "static" , folder_name, current_user.b_certificate))
    # Save new picture
    if f_ext != '.pdf':
        output_size= (125,125)
        i=Image.open(form_file)
        i.thumbnail(output_size)
        i.save(picture_path)
    else:
        form_file.save(picture_path)

    return file_name
@app.context_processor
def utility_processor():
    def current_year():
        return datetime.today().year
    return dict(current_year=current_year)
def tableDisplay(elemento, form):
    r = dict()
    if elemento == "laboratorista" and current_user.role == 'admin':
        r = {
        'table_items': Laboratorista.query.filter_by(username=form.value.data),
        'search_item' : 'username',
        'table_header' : Laboratorista.__table__.columns.keys()
        }
    elif elemento == "clientes":
        r = {
        'table_items': Cliente.query.filter_by(rfc=form.value.data),
        'search_item' : 'rfc',
        'table_header' : Cliente.__table__.columns.keys()
        }
    elif elemento == "equipo":
        r = {
        'table_items': EquipoLab.query.filter_by(clave=form.value.data),
        'search_item' : 'clave',
        'table_header' : EquipoLab.__table__.columns.keys()
        }
    elif elemento == "certificados":
        r = {
        'table_items': Certificado.query.filter_by(ncertificado=form.value.data),
        'search_item' : 'N Certificado',
        'table_header' : Certificado.__table__.columns.keys()
        }
    elif elemento == "registro":
        r = {
        'table_items': Inspeccion.query.filter_by(idi=form.value.data),
        'search_item' : 'Idi',
        'table_header' : Inspeccion.__table__.columns.keys()
        }
    else:
       r = {'error message' : 'Ruta no Valida', 'type':'info'}
    return r
def tableDisplayAll(elemento, form):
    r = dict()
    if elemento == "laboratorista" and current_user.role == 'admin':
        r = {
        'table_items': Laboratorista.query.all(),
        'search_item' : 'username',
        'table_header' : Laboratorista.__table__.columns.keys()
        }
    elif elemento == "clientes":
        r = {
        'table_items': Cliente.query.all(),
        'search_item' : 'rfc',
        'table_header' : Cliente.__table__.columns.keys()
        }
    elif elemento == "equipo":
        r = {
        'table_items': EquipoLab.query.all(),
        'search_item' : 'clave',
        'table_header' : EquipoLab.__table__.columns.keys()
        }
    elif elemento == "certificados":
        r = {
        'table_items': Certificado.query.all(),
        'search_item' : 'N Certificado',
        'table_header' : Certificado.__table__.columns.keys()
        }
    elif elemento == "registro":
        r = {
        'table_items': Inspeccion.query.all(),
        'search_item' : 'Idi',
        'table_header' : Inspeccion.__table__.columns.keys()
        }
    else:
       r = {'error message' : 'Ruta no Valida', 'type':'info'}
    
    return r
def TableValues(elemento):

    if elemento == "laboratorista" and current_user.role == 'admin':
        return {'query_result' : Laboratorista(), 'search_item' : 'username', 'table_header' : Laboratorista.__table__.columns.keys()}
    elif elemento == "clientes":
        return {'query_result' : Cliente(), 'search_item' : 'rfc', 'table_header' : Cliente.__table__.columns.keys() }
    elif elemento == "equipo":
        return {'query_result' : EquipoLab(),'search_item' : 'clave', 'table_header' : EquipoLab.__table__.columns.keys() }
    elif elemento == "certificados":
        return {'query_result' : Certificado, 'search_item' : 'ncertificado', 'table_header' : Certificado.__table__.columns.keys() }
    elif elemento == "registro":
        return {'query_result' : Inspeccion(),' search_item' : 'idi', 'table_header' : Inspeccion.__table__.columns.keys() }
    else:
        return {'error message' : 'Query Invalido', 'type':'alert'}

    
    

@app.route('/login', methods=["GET","POST"])
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
    form = Buscar()
    modalForm = {
            'laboratorista' : RegiseterLab(),
            'clientes' : RegisterCliente()
    }
    if modalForm[elemento].validate_on_submit():
        pass
    else:
        if form.validate_on_submit():
            # Revisar que tabla buscar:
            table = tableDisplay(elemento, form)
        else:
            table = tableDisplayAll(elemento, form)
        
        if 'error message' in table:
            flash(table['error message'], table['type'])
            return redirect(url_for('menu'))
        
        return render_template("buscador.html", 
        elemento=str(elemento).capitalize(), 
        table_items=table['table_items'], 
        table_header=table['table_header'], 
        search_item = table['search_item'],
        # Formularios a usar
        form=form, 
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
    table = TableValues(elemento)['query_result']
    result = table.query.get(value_id)
    db.session.delete(result)
    db.session.commit()
    flash(f"El conepto con ID: {value_id} fue eliminado ", 'info')

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
