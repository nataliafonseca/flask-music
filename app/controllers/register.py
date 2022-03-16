from app import app, db
from app.models.form import Form
from app.models.user import User
from bcrypt import gensalt, hashpw
from flask import redirect, render_template, url_for
from flask_login import login_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Form()
    username_taken = False

    if form.validate_on_submit():
        username_taken = (
            len(User.query.filter_by(username=f'{form.username.data}').all())
            > 0
        )

        if not username_taken:
            hashed_password = hashpw(
                form.password.data.encode('utf8'), gensalt()
            )
            new_user = User(form.username.data, hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('application'))

    return render_template(
        'register.html', form=form, username_taken=username_taken
    )
