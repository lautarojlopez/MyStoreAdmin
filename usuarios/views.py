from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login.utils import login_required, login_user, logout_user
from .models import Usuario
from .forms import FormLogin, FormRegistro
import bcrypt

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/crear-cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'GET':
        form = FormRegistro()
        return render_template('crear-cuenta.html', form=form)
    if request.method == 'POST':
        form_registro = FormRegistro(request.form)
        if form_registro.validate():
            try:
                nuevo_usuario = Usuario(email=request.form['email'], password=request.form['password'])
                nuevo_usuario.save()
                flash('Tu cuenta ha sido creada.', 'success')
                return redirect(url_for('usuarios.iniciar_sesion'))
            except:
                flash('Ups.. Algo salió mal. Intentalo nuevamente.', 'error')
                return redirect(url_for('usuarios.crear_cuenta'))
        else:
            for error in form_registro.errors.values():
                flash(error[0], 'error')
            return redirect(url_for('usuarios.crear_cuenta'))
        
@usuarios.route('/iniciar-sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'GET':
        form = FormLogin()
        return render_template('iniciar-sesion.html', form=form)
    if request.method == "POST":
        form_login = FormLogin(request.form)
        if form_login.validate():
            user = Usuario.objects(email=request.form['email']).first()
            if user:
                valid_password = bcrypt.checkpw(request.form['password'].encode('utf-8'), user['password'].encode('utf-8'))
                if valid_password:
                    login_user(user)
                    return redirect(url_for('general.index'))
                else:
                    # Si la contraseña no es correcta
                    flash('Contraseña incorrecta.', 'error')
                    return redirect(url_for('usuarios.iniciar_sesion'))
            else:
                # Si el usuario no existe
                flash('El usuario no existe.', 'error')
                return redirect(url_for('usuarios.iniciar_sesion'))
        else:
            for error in form_login.errors.values():
                flash(error[0], 'error')
            return redirect(url_for('usuarios.iniciar_sesion'))

@usuarios.route('/cerrar-sesion')
@login_required
def cerrar_sesion():
    logout_user()
    return redirect(url_for('usuarios.iniciar_sesion'))