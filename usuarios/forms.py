import bcrypt
from flask_wtf import FlaskForm
from wtforms import Form, EmailField, validators, PasswordField
from .models import Usuario

class FormRegistro(FlaskForm):
    email = EmailField(validators=[validators.InputRequired(message='Ingresa tu e-mail.'), validators.Email('El e-mail ingresado no es válido.')])
    password = PasswordField(validators=[validators.InputRequired(message='Ingresa una contraseña.'), validators.Length(min=8, max=20, message='La contraseña es debe tener al menos 8 caracteres.')])
    password_confirm = PasswordField(validators=[validators.InputRequired('Repite tu contraseña'), validators.EqualTo('password', message='Las contraseñas no coinciden.')])

    def validate_email(self, email):
        existing_email = Usuario.objects(email=email.data)
        if existing_email:
            raise validators.ValidationError('El e-mail ya está registrado.')

class FormLogin(FlaskForm):
    email = EmailField(validators=[validators.InputRequired(message='Ingresa tu e-mail.')])
    password = PasswordField(validators=[validators.InputRequired(message='Ingresa una contraseña.')])

class FormForgotPassword(FlaskForm):
    email = EmailField(validators=[validators.InputRequired(message='Ingresa tu e-mail.'), validators.Email('El e-mail ingresado no es válido.')])

class FormRestaurarPassword(FlaskForm):
    password = PasswordField(validators=[validators.InputRequired(message='Ingresa una contraseña.'), validators.Length(min=8, max=20, message='La contraseña es debe tener al menos 8 caracteres.')])
    password_confirm = PasswordField(validators=[validators.InputRequired('Repite tu contraseña'), validators.EqualTo('password', message='Las contraseñas no coinciden.')])
