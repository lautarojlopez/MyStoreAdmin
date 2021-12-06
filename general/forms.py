from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, FileField
from wtforms.validators import *

class FormAgregarProducto(FlaskForm):
    nombre = StringField(validators=[Length(max=250), InputRequired()])
    codigo = StringField(validators=[Length(max=250), InputRequired()])
    precio = FloatField(InputRequired())
    stock = IntegerField(InputRequired())
    imagen = FileField()