from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from processing.utils import createToken
from datetime import datetime, timedelta
from flask import g

db = g.db


def createUserFromJson(json):
    id = db.session.query(db.func.max(User.id)).scalar()
    if id is None:
        id = 1
    else:
        id += 1
    user = getUser(email=json['email'])
    if user is not None:
        return False

    user = User(id=id,
                email=json['email'],
                hashed_password=generate_password_hash(json['password'])
                )
    db.session.add(user)
    db.session.commit()
    return True


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    access_token = db.Column(db.String(255))
    access_token_expire = db.Column(db.DateTime)
    refresh_token = db.Column(db.String(255))
    refresh_token_expire = db.Column(db.DateTime)

    def __repr__(self):
        return F"email: {self.email}"

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def log_in(self):
        self.access_token = createToken()
        self.access_token_expire = datetime.utcnow() + timedelta(minutes=1)
        self.refresh_token = createToken()
        self.refresh_token_expire = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        return self.access_token, self.refresh_token


def isAuthenticated(access_token):
    user = db.session.query(User).filter(User.access_token == access_token, db.func.now() < User.access_token_expire).first()
    if user is not None:
        return True
    return False


def refreshToken(refresh_token):
    user = db.session.query(User).filter(User.refresh_token == refresh_token, db.func.now() < User.refresh_token_expire).first()
    if user is not None:
        return user.log_in()
    return False


def logoutUser(refresh_token):
    user = db.session.query(User).filter(User.refresh_token == refresh_token, db.func.now() < User.refresh_token_expire).first()
    if user is not None:
        user.refresh_token_expire = None
        user.access_token_expire = None
        db.session.commit()


def getUser(**kwargs):
    return User.query.filter_by(**kwargs).first()