from wtforms import Form, EmailField, validators, PasswordField

class FormRegistro(Form):
    email = EmailField(validators=[validators.InputRequired(message='Ingresa tu e-mail.'), validators.Email('El e-mail ingresado no es válido.')])
    password = PasswordField(validators=[validators.InputRequired(message='Ingresa una contraseña.'), validators.Length(min=8, max=20, message='La contraseña es debe tener al menos 8 caracteres.')])
    password_confirm = PasswordField(validators=[validators.InputRequired('Repite tu contraseña'), validators.EqualTo('password', message='Las contraseñas no coinciden.')])