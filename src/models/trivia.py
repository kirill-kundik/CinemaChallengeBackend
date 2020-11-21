import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

trivias_questions = db.Table(
    'trivias_questions', db.metadata,
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), nullable=False),
    db.Column('trivia_id', db.Integer, db.ForeignKey('trivia.id'), nullable=False)
)


class Trivia(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "trivia"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    first_player_score = db.Column(db.Integer, nullable=False, default=0)
    second_player_score = db.Column(db.Integer, nullable=False, default=0)

    completed = db.Column(db.Boolean, nullable=False, default=False)

    achievement_id = db.Column(db.Integer, db.ForeignKey('achievement.id'))

    user_id = db.Column(db.String, db.ForeignKey('user.oid'), nullable=False)
    second_player_id = db.Column(db.String, db.ForeignKey('user.oid'))

    user = db.relationship('User', foreign_keys=[user_id])
    second_player = db.relationship('User', foreign_keys=[second_player_id])

    submitted_answers = db.relationship('SubmittedAnswer')

    questions = db.relationship(
        "Question", secondary=trivias_questions
    )
