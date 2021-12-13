from usuarios.models import Usuario
from mongoengine import Document, StringField, FloatField, IntField, ReferenceField, DateTimeField
import datetime

class Producto(Document):
    meta = {'collection': 'productos'}

    nombre = StringField(max_length=250, null=False)
    codigo = StringField(max_length=250, null=False)
    precio = FloatField(null=False)
    stock = IntField(null=False)
    imagen = StringField() # Solo almacena la ruta de la imagen
    usuario = ReferenceField(Usuario)
    # Timestamps
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.nombre} - {self.codigo}'
    
    def eliminar_stock(self, cantidad):
        self.stock = self.stock - cantidad
    def reponer_stock(self, cantidad):
        self.stock = self.stock + cantidad
    