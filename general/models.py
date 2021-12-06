from mongoengine import Document, StringField, FloatField, IntField, FileField
from mongoengine.fields import ImageField

class Producto(Document):
    meta = {'collection': 'productos'}

    nombre = StringField(max_length=250, null=False)
    codigo = StringField(max_length=250, null=False)
    precio = FloatField(null=False)
    stock = IntField(null=False)
    imagen = ImageField()
    