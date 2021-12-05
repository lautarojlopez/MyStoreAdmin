from mongoengine import *
from mongoengine import signals
from mongoengine.document import Document
from mongoengine.fields import EmailField, StringField
import bcrypt

class Usuario(Document):
    meta = {'collection': 'usuarios'}
    email = EmailField(required=True, unique=True, blank=False, null=False)
    password = StringField(max_length=80, required=True, blank=False, null=False)
    
    # Encripta la contraseña antes de guardar por primera vez
    @classmethod
    def pre_save_post_validation(cls, sender, document, *args, **kwargs):
        # Si la contraseña ya esta encriptada, entonces no la encripta
        if type(document.password) is not 'bytes':
            document.password = bcrypt.hashpw(document.password.encode('utf-8'), bcrypt.gensalt())

signals.pre_save_post_validation.connect(Usuario.pre_save_post_validation, sender=Usuario)