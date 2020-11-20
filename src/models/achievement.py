from . import db
from .abc import BaseModel, MetaBaseModel


class Achievement(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "achievement"

    to_json_filter = ('questions', 'users')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    short_description = db.Column(db.String)
    long_description = db.Column(db.String)
    difficulty = db.Column(db.Integer)
    image_src = db.Column(db.String)
    bg_image_src = db.Column(db.String)

    users = db.relationship("Obtained", back_populates="achievement")
    questions = db.relationship("Question", back_populates="achievement")

    def __init__(
            self, name, short_description, long_description, difficulty, image_src, bg_image_src
    ):
        """ Create a new User """
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.difficulty = difficulty
        self.image_src = image_src
        self.bg_image_src = bg_image_src
