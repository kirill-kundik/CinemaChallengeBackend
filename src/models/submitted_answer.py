import datetime

from . import db
from .abc import BaseModel, MetaBaseModel


class SubmittedAnswer(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "submitted_answer"

    to_json_filter = ('trivia',)

    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.oid'), nullable=False)
    trivia_id = db.Column(db.Integer, db.ForeignKey('trivia.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    answer = db.relationship('Answer', back_populates='submitted_answers')
