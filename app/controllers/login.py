from app import app
from app.models.form import Form
from app.models.user import User
from bcrypt import checkpw
from flask import redirect, render_template, url_for
from flask_login import login_user, logout_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Form()
    authentication_error = False

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and checkpw(form.password.data.encode('utf8'), user.password):
            login_user(user)
            return redirect(url_for('application'))
        else:
            authentication_error = True

    return render_template(
        'login.html', form=form, authentication_error=authentication_error
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
