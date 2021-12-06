from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from wtforms.validators import URL
from .models import Producto

from general.forms import FormAgregarProducto

general = Blueprint('general', __name__)

@general.route('/')
@login_required
def index():
    return render_template('index.html')

@general.route('/productos')
@login_required
def productos():
    return render_template('productos.html')

@general.route('/productos/agregar', methods=['GET', 'POST'])
@login_required
def agregar_producto():
    if request.method == "GET":
        form = FormAgregarProducto()
        return render_template('agregar-producto.html', form=form)
    if request.method == "POST":
        form_producto = FormAgregarProducto(request.form, imagen=request.files)
        if form_producto.validate_on_submit():
            try:
                
                producto = Producto(nombre=form_producto['nombre'].data, codigo=form_producto['codigo'].data, precio=float(form_producto['precio'].data), stock=form_producto['stock'].data, imagen=form_producto['imagen'].data)
                producto.save()
            except Exception as e:
                print(e)
            return redirect(url_for('general.agregar_producto'))
