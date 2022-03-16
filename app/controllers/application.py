from app import app
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required


@app.route('/application', methods=['GET'])
def application():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.username.upper()
    return render_template('application.html', username=username)
