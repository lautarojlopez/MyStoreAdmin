from flask import Flask, render_template
from usuarios.routes import usuarios
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)

# Secret Key
app.secret_key = os.environ.get('SECRET_KEY')

# Connection to MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get('DB_NAME'),
    'host': os.environ.get('DB_HOST')
}
db = MongoEngine(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=8000)