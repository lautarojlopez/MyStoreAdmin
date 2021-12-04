from flask import Flask, render_template
from usuarios.routes import usuarios

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=8000)