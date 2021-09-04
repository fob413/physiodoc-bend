from datetime import datetime

from .model_mixin import ModelMixin
from models import db
from .helper import generate_password_hash, check_password_hash


class AdminUser(ModelMixin):

    __tablename__ = 'admin_user'

    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.Binary, nullable=False)

    def __repr__(self):
        return '<AdminUser %r>' % self.email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password.encode())
