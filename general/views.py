from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from shortuuid import uuid

from clientes.views import clientes
from usuarios.models import Usuario
from .models import Producto
from pedidos.models import Pedido
from clientes.models import Cliente
import os

from general.forms import FormAgregarProducto

general = Blueprint('general', __name__)

# Ver el inicio
@general.route('/')
@login_required
def index():
    pedidos = Pedido.objects(usuario=current_user)[:6]
    productos = Producto.objects(usuario=current_user)[:5]
    clientes =  Cliente.objects(usuario=current_user)[:5]
    return render_template('index.html', pedidos=pedidos, productos=productos, clientes=clientes)

@general.route('/buscar')
@login_required
def buscar():
    print(request.args)
    # Buscar producto
    if request.args.get('producto'):
        busqueda = request.args.get('producto')
        productos = Producto.objects(nombre__icontains=busqueda, usuario=current_user)
        return render_template('buscar.html', productos=productos, busqueda=busqueda)
    # Buscar cliente
    if request.args.get('cliente'):
        busqueda = request.args.get('cliente')
        clientes = Cliente.objects(nombre__icontains=busqueda, usuario=current_user)
        return render_template('buscar.html', clientes=clientes, busqueda=busqueda)
    return render_template('buscar.html')

# Ver todos los productos
@general.route('/productos/')
@login_required
def productos():
    productos = Producto.objects(usuario=current_user).order_by('-updated_at')
    return render_template('productos.html', productos = productos)

# Agregar un nuevo producto
@general.route('/productos/agregar', methods=['GET', 'POST'])
@login_required
def agregar_producto():
    if request.method == "GET":
        form = FormAgregarProducto()
        return render_template('agregar-producto.html', form=form)
    if request.method == "POST":
        form_producto = FormAgregarProducto(request.form, imagen=request.files)
        if form_producto.validate():
            try:
                # Guarda la imagen
                if request.files['imagen']:
                    imagen = request.files['imagen']
                    imagen_filename = secure_filename(f'{uuid()}-{imagen.filename}')
                    imagen.save(f'./static/uploads/{imagen_filename}')
                else:
                    imagen_filename = 'default.png'
                # Inserta el producto en la base de datos
                producto = Producto(nombre=form_producto['nombre'].data, codigo=form_producto['codigo'].data, precio=float(form_producto['precio'].data), stock=int(form_producto['stock'].data), imagen=imagen_filename, usuario=current_user)
                producto.save()
                # Redirecciona con mensaje de ??xito
                flash('Producto agregado.', 'success')
                return redirect(url_for('general.productos'))
            except:
                # Redirecciona con mensaje de error
                flash('Ups.. Algo sali?? mal. Intentalo nuevamente.', 'error')
                return redirect(url_for('general.agregar_producto'))
        else:
            # Muestra los errores de validaci??n del formulario
            for error in form_producto.errors.values():
                flash(error[0], 'error')
            return redirect(url_for('general.agregar_producto'))

# Eliminar producto
@general.route('/productos/eliminar/<string:id>', methods=['GET', 'POST'])
@login_required
def eliminar_producto(id):

    try:
        producto = Producto.objects(id=id).first()
        if producto.usuario.id != current_user.id:
            return redirect(url_for('general.error_401'))
    except:
        # Redirecciona con mensaje de error
        flash('Ups.. Algo sali?? mal. Intentalo nuevamente.', 'error')
        return redirect(url_for('general.productos'))

    if request.method == "GET":
        return render_template('eliminar-producto.html', producto=producto)
    if request.method == "POST":
        try:
            if producto.imagen != 'default.png':
                os.remove(f'static/uploads/{producto.imagen}')
            producto.delete()
            # Redirecciona con mensaje de ??xito
            flash('Producto eliminado.', 'success')
            return redirect(url_for('general.productos'))
        except:
            # Redirecciona con mensaje de error
            flash('Ups.. Algo sali?? mal. Intentalo nuevamente.', 'error')
            return redirect(url_for('general.productos'))

# Editar un producto
@general.route('/productos/editar/<string:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    try:
        producto = Producto.objects(id=id).first()
        if producto.usuario.id != current_user.id:
            return redirect(url_for('general.error_401'))
    except:
        # Redirecciona con mensaje de error
        flash('Ups.. Algo sali?? mal. Intentalo nuevamente.', 'error')
        return redirect(url_for('general.productos'))
    
    if request.method == "GET":
        form = FormAgregarProducto()
        return render_template('editar-producto.html',form=form, producto=producto)
    if request.method == "POST":
        form_producto = FormAgregarProducto(request.form, imagen=request.files)
        if form_producto.validate():
            producto.nombre = form_producto['nombre'].data
            producto.codigo = form_producto['codigo'].data
            producto.precio = float(form_producto['precio'].data)
            producto.stock = form_producto['stock'].data
            if request.files['imagen']:
                if producto.imagen != 'default.png':
                    os.remove(f'static/uploads/{producto.imagen}')
                imagen = request.files['imagen']
                imagen_filename = secure_filename(f'{uuid()}-{imagen.filename}')
                imagen.save(f'./static/uploads/{imagen_filename}')
                producto.imagen = imagen_filename
            producto.save()
            flash('Producto editado.', 'success')
            return redirect(url_for('general.productos'))
        else:
            # Muestra los errores de validaci??n del formulario
            for error in form_producto.errors.values():
                flash(error[0], 'error')
            return redirect(url_for('general.editar_producto', id=id))

@general.route('/401', methods=['GET', 'POST'])
@login_required
def error_401():
    return render_template('401.html')