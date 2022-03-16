from app import app
from flask import redirect, url_for
from flask_login import current_user


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('application'))
    else:
        return redirect(url_for('login'))
