from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required

general = Blueprint('general', __name__)

@general.route('/')
@login_required
def index():
    return render_template('index.html')