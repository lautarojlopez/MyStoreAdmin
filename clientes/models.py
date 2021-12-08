from usuarios.models import Usuario
from mongoengine import Document, StringField, DateTimeField, EmailField, ReferenceField
import datetime

class Cliente(Document):
    meta = {'collection': 'clientes'}
    nombre = StringField(max_length=50, null=False)
    email = EmailField(max_length=50, null=False)
    direccion = StringField(max_length=50, null=False)
    telefono = StringField(max_length=50, null=False)
    usuario = ReferenceField(Usuario)
    # TODO - Crear relacion one to many de pedidos
    # Timestamps
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    