from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, FileField, validators
from wtforms.validators import *
from flask_login import current_user
from general.models import Producto

class FormAgregarProducto(FlaskForm):
    nombre = StringField(validators=[Length(max=250), InputRequired('Escribe el nombre del producto.')])
    codigo = StringField(validators=[Length(max=250), InputRequired('Escribe el código del producto.')])
    precio = FloatField(InputRequired('Indica el precio del producto.'))
    stock = IntegerField(InputRequired('Indica el stock'))
    imagen = FileField()

    # Verifica el formato de la imagen
    def validate_imagen(self, imagen):
        if imagen.data['imagen']:
            filename = imagen.data['imagen'].filename
            if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpeg', 'jpg', 'png'}):
                raise validators.ValidationError('El archivo no es una imagen.')