from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user
from usuarios.models import Usuario
import os

# Views
from usuarios.views import usuarios
from general.views import general

app = Flask(__name__)

# Secret Key
app.secret_key = os.environ.get('SECRET_KEY')

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'usuarios.iniciar_sesion'
@login_manager.user_loader
def load_user(user_id):
    user = Usuario.objects.get(id=user_id)
    if user:
        return user
    else:
        return None

# Connection to MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get('DB_NAME'),
    'host': os.environ.get('DB_HOST')
}
db = MongoEngine(app)

# File Uploads
app.config['UPLOAD_FOLDER'] = './static/media/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1000 * 1000

# Routes
app.register_blueprint(usuarios)
app.register_blueprint(general)


if __name__ == '__main__':
    app.run(debug=True, port=8000)