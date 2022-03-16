from app import db, lm


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


@lm.user_loader
def load_user(user):
    return User.query.get(user)
