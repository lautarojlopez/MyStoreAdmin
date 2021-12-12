from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_login.utils import login_required, current_user
from werkzeug.utils import redirect
from clientes.models import Cliente
from general.models import Producto
from usuarios.models import Usuario
from pedidos.models import Pedido
from pedidos.forms import FormAgregarPedido

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/')
@login_required
def ver_pedidos():
    pedidos = Pedido.objects(usuario=current_user)
    return render_template('pedidos.html', pedidos=pedidos)

@pedidos_bp.route('/agregar', methods=['GET', 'POST'])
@login_required
def agregar_pedido():
    productos = Producto.objects(usuario=current_user)
    clientes = Cliente.objects(usuario=current_user)

    if request.method == 'GET':
        form = FormAgregarPedido()
        return render_template('agregar-pedido.html', productos=productos, clientes=clientes, form=form)
    if request.method == 'POST':
        try:
            form_pedido = FormAgregarPedido()
            if form_pedido.validate():
                pedido = Pedido()
                pedido.cliente = Cliente.objects.get(id=request.form['cliente'])
                pedido.usuario = current_user
                for prod in request.form.getlist('producto'):
                    producto = Producto.objects.get(id=prod)
                    pedido.productos.append(producto)
                for cantidad in request.form.getlist('cantidad'):
                    pedido.cantidades.append(cantidad)
                pedido.save()
                flash('Pedido agregado.', 'success')
                return redirect(url_for('pedidos.ver_pedidos'))
            else:
                # Muestra los errores de validación del formulario
                for error in form_pedido.errors.values():
                    flash(error[0], 'error')
                return redirect(url_for('pedidos.agregar_pedido'))
        except:
            # Redirecciona con mensaje de error
            flash('Ups.. Algo salió mal. Intentalo nuevamente.', 'error')
            return redirect(url_for('general.productos'))

# Eliminar un pedido
@pedidos_bp.route('/eliminar/<string:id>', methods=['GET', 'POST'])
@login_required
def eliminar_pedido(id):
    
    pedido = Pedido.objects.get(id=id)

    # Si no es el creador del pedido, redirecciona a 401
    if pedido.usuario.id != current_user.id:
        return render_template('401.html')
    
    if request.method == "GET":
        return render_template('eliminar-pedido.html', pedido=pedido)
    if request.method == "POST":
        try:
            pedido.delete()
            # Redirecciona con mensaje de éxito
            flash('Pedido eliminado.', 'success')
            return redirect(url_for('pedidos.ver_pedidos'))
        except:
            # Redirecciona con mensaje de error
            flash('Ups.. Algo salió mal. Intentalo nuevamente.', 'error')
            return redirect(url_for('clientes.clientes'))