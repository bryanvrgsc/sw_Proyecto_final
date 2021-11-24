from flask import render_template, request, redirect, session, url_for, flash, Markup
from webapp import app #, db, bcrypt
from webapp.forms import  Login
# from webapp.models import *
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
    if request.method == 'POST':
        if form.username.data == 'admin':
            user = 1
        if form.username.data == 'regular':
            user = 0
        return redirect(url_for('menu', user=user))

    
    return render_template("login.html", title="Login", form=form)



@app.route("/menu/<user>")
def menu(user):
    user =int(user)
    return render_template("menu.html", user_type=user)


@app.route("/buscador/<elemento>")
def buscador(elemento):

    return elemento





