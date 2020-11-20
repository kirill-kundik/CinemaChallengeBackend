import datetime

from . import db
from .abc import BaseModel, MetaBaseModel


class Obtained(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "obtained"

    to_json_filter = ('user', 'achievement')

    user_id = db.Column(db.String, db.ForeignKey('user.oid'), primary_key=True)
    achievement_id = db.Column(db.Integer, db.ForeignKey('achievement.id'), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    user = db.relationship("User", back_populates="achievements")
    achievement = db.relationship("Achievement", back_populates="users")
