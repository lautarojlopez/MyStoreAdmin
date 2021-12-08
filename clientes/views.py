from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import FormAgregarCliente
from .models import Cliente

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/', methods=['GET', 'POST'])
@login_required
def clientes():
    clientes = Cliente.objects(usuario=current_user)
    return render_template('clientes.html', clientes=clientes)

@clientes_bp.route('/agregar', methods=['GET', 'POST'])
@login_required
def agregar_cliente():
    if request.method == 'GET':
        form = FormAgregarCliente()
        return render_template('agregar-cliente.html', form=form)
    if request.method == 'POST':
        form_cliente = FormAgregarCliente(request.form)
        if form_cliente.validate():
            try:
                cliente = Cliente()
                cliente.nombre = form_cliente['nombre'].data
                cliente.email = form_cliente['email'].data
                cliente.direccion = form_cliente['direccion'].data
                cliente.telefono = form_cliente['telefono'].data
                cliente.usuario = current_user
                cliente.save()
                # Redirecciona con mensaje de éxito
                flash('Cliente agregado.', 'success')
                return redirect(url_for('clientes.clientes'))
            except:
                # Redirecciona con mensaje de error
                flash('Ups.. Algo salió mal. Intentalo nuevamente.', 'error')
                return redirect(url_for('clientes.agregar_cliente'))
        else:
            # Muestra los errores de validación del formulario
            for error in form_cliente.errors.values():
                flash(error[0], 'error')
            return redirect(url_for('clientes.agregar_cliente'))
