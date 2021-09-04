from datetime import datetime

from .model_mixin import ModelMixin
from models import db


class SampleModel(ModelMixin):

    __tablename__ = 'sample_model'

    id = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return '<SampleModel %r>' % self.id
