from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from .models import Usuario
from .forms import FormRegistro

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/crear-cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'GET':
        return render_template('crear-cuenta.html')
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
                return redirect(url_for('crear_cuenta'))
        else:
            for error in form_registro.errors.values():
                flash(error, 'error')
            return redirect(url_for('usuarios.crear_cuenta'))
        
        
        

@usuarios.route('/iniciar-sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'GET':
        return render_template('iniciar-sesion.html')