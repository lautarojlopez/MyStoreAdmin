from flask import Flask, Blueprint, render_template, request

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/crear-cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'GET':
        return render_template('crear-cuenta.html')
    if request.method == 'POST':
        return f'{request.form.get("password")}'

@usuarios.route('/iniciar-sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'GET':
        return render_template('iniciar-sesion.html')