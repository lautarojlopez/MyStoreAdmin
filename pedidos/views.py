from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_login.utils import login_required, current_user
from werkzeug.utils import redirect
from clientes.models import Cliente
from general.models import Producto
from usuarios.models import Usuario
from pedidos.models import Pedido

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
        pedidos = Pedido.objects()
        return render_template('agregar-pedido.html', productos=productos, clientes=clientes)
    if request.method == 'POST':
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