from datetime import datetime

from .model_mixin import ModelMixin
from models import db, AdminUser


class Post(ModelMixin):

    __tablename__ = 'post'

    id = db.Column(db.String, primary_key=True)
    post_image_url = db.Column(db.String(), nullable=True)
    post = db.Column(db.String(), nullable=False)
    is_published = db.Column(db.Boolean(), default=False, nullable=False)
    admin_user_id = db.Column(db.String, db.ForeignKey(AdminUser.id), nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.id
