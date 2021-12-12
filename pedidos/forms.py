from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import *

class FormAgregarPedido(FlaskForm):
    cliente = StringField(validators=[InputRequired('Selecciona un cliente.')])
    producto = StringField(validators=[InputRequired('Selecciona un producto.')])