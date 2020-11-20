from . import db
from .abc import BaseModel, MetaBaseModel


class Question(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "question"

    to_json_filter = ('achievement',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image_url = db.Column(db.String)
    tip = db.Column(db.String)

    achievement_id = db.Column(db.Integer, db.ForeignKey('achievement.id'), nullable=False)
    achievement = db.relationship('Achievement', back_populates='questions')

    answers = db.relationship('Answer', back_populates='question')

    def __init__(
            self, title, image_url, tip
    ):
        """ Create a new User """
        self.title = title
        self.image_url = image_url
        self.tip = tip
