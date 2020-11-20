import datetime

from . import db
from .abc import BaseModel, MetaBaseModel


class Trivia(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "trivia"

    to_json_filter = ('achievement',)

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    user_id = db.Column(db.String, db.ForeignKey('user.oid'), nullable=False)
    second_player_id = db.Column(db.String, db.ForeignKey('user.oid'))

    user = db.relationship('User', foreign_keys=[user_id])
    second_player = db.relationship('User', foreign_keys=[second_player_id])
