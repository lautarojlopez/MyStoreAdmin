from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from usuarios.models import Usuario
import os

# Views
from usuarios.views import usuarios
from general.views import general
from clientes.views import clientes_bp
from pedidos.views import pedidos_bp

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
app.register_blueprint(clientes_bp, url_prefix='/clientes')
app.register_blueprint(pedidos_bp, url_prefix='/pedidos')

if __name__ == '__main__':
    app.run(debug=True, port=8000)