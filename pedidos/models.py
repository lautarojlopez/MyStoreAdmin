from mongoengine.document import EmbeddedDocument
from mongoengine.fields import DictField, IntField, ListField
from mongoengine import CASCADE, PULL
from usuarios.models import Usuario
from clientes.models import Cliente
from general.models import Producto
from mongoengine import Document, ReferenceField, DateField
import datetime

class Pedido(Document):
    meta = {'collection': 'pedidos'}
    cliente = ReferenceField(Cliente, reverse_delete_rule=CASCADE)
    # Lista de productos y su cantidad
    productos = ListField(ReferenceField(Producto))
    cantidades = ListField(IntField())
    usuario = ReferenceField(Usuario)
    # Timestamps
    created_at = DateField(default=datetime.datetime.now().date())