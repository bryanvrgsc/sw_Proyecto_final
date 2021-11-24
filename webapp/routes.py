from flask import render_template, request, redirect, session, url_for, flash, Markup
from webapp import app, db, bcrypt
from webapp.forms import  Login
from webapp.models import *
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from datetime import datetime

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


@app.route('/', methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
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


@app.route("/menu")
def menu():
    if current_user.is_authenticated:
        user_type = current_user.role
        return render_template("menu.html", user_type=user_type, menu_items=menu)
    else:
        return redirect(url_for("home"))


@app.route("/buscador/<elemento>")
def buscador(elemento):
    if current_user.is_authenticated:
        table_items = []
        table_header = []
         # Revisar que tabla buscar:
        if elemento == "laboratorista":
            table_items = Laboratorista.query.all()
            table_header = Laboratorista.__table__.columns.keys()
        elif elemento == "clientes":
            table_items = Cliente.query.all()
            table_header = Cliente.__table__.columns.keys()
        elif elemento == "equipo":
            table_items = EquipoLab.query.all()
            table_header = EquipoLab.__table__.columns.keys()
        elif elemento == "certificados":
            table_items = Certificado.query.all()
            table_header = Certificado.__table__.columns.keys()
        elif elemento == "registro":
            table_items = Inspeccion.query.all()
            table_header = Inspeccion.__table__.columns.keys()
        else:
            flash("Ruta no valida", "info")
            return redirect(url_for('home'))
        

        return render_template("buscador.html", elemento=str(elemento).capitalize(), table_items=table_items, table_header=table_header)
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('home'))


# Acciones de tabla
@app.route("/Eliminar/<elemento>/<valor_id>")
def Eliminar(elemento,valor_id):
    if current_user.is_authenticated:

        return redirect(url_for('buscador', elemento))
    else:
        return redirect(url_for("home"))


# @app.route("/logout")
# def logout():
#     if current_user.is_authenticated:
        
#     return redirect(url_for('buscador', elemento))

# @app.route("/logout")
# def logout():
#     if current_user.is_authenticated:
#         l
#     return redirect(url_for('buscador', elemento))
    


# Creacion de certificado
@app.route("/creacion-certificado")
def creacion_certificado():
    if current_user.is_authenticated:
        pass



