from . import db
from .abc import BaseModel, MetaBaseModel


class Answer(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "answer"

    to_json_filter = ('question', 'submitted_answers')

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    is_right = db.Column(db.Boolean, default=False)

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question = db.relationship('Question', back_populates='answers')

    submitted_answers = db.relationship('SubmittedAnswer', back_populates='answer')

    def __init__(
            self, text, is_right
    ):
        """ Create a new User """
        self.text = text
        self.is_right = is_right
