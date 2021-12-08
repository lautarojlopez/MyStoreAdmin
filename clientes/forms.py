from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import *

class FormAgregarCliente(FlaskForm):
    nombre = StringField(validators=[InputRequired('Escribe el nombre del cliente'), Length(max=50, message='El nombre es demasiado largo.')])
    email = EmailField(validators=[InputRequired('Escribe el e-mail del cliente.'), Length(max=50, message='El e-mail es demasiado largo.')])
    direccion = StringField(validators=[InputRequired('Escribe la dirección del cliente.'), Length(max=50, message='La dirección es demasiado larga.')])
    telefono = StringField(validators=[InputRequired('Escribe el teléfono del cliente.'), Length(max=50, message='El teléfono es demasiado largo.')])


