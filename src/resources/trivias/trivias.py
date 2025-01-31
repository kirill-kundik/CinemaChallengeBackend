"""
Define the REST verbs relative to the users
"""

from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy import and_, text, or_

from models import Trivia, db, Question
from repositories import AchievementRepository
from services import with_auth
from util import render_resource, render_error, parse_params


class TriviasResources(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @parse_params(
        Argument("achievement_id", location="json", type=int, default=None, help="Achievement_id if it for the test")
    )
    @with_auth
    def post(user, achievement_id, **_kwargs):
        """ Return an user key information based on his name """
        if achievement_id:
            trivia = Trivia.query.filter(
                and_(Trivia.completed == False,
                     and_(
                         Trivia.user_id == user.oid,
                         Trivia.achievement_id == achievement_id
                     ))
            ).first()
        else:
            trivia = Trivia.query.filter(
                and_(
                    and_(Trivia.completed == False,
                         or_(
                             Trivia.user_id == user.oid,
                             Trivia.second_player_id == user.oid
                         )),
                    Trivia.achievement_id == None
                )
            ).first()

        if trivia:
            return render_resource(trivia)

        try:
            if achievement_id:
                trivia = Trivia(user_id=user.oid, achievement_id=achievement_id)
                trivia.questions = AchievementRepository.get(achievement_id).questions

            else:
                trivia = Trivia.query.filter(
                    and_(and_(
                        Trivia.second_player_id == None,
                        Trivia.achievement_id == None
                    ), or_(
                        Trivia.second_player_id != user.oid,
                        Trivia.user_id != user.oid
                    ))
                ).first()

                if not trivia:
                    trivia = Trivia(user_id=user.oid)
                else:
                    trivia.second_player_id = user.oid

                    for question in Question.query.from_statement(
                            text("select * from question order by random() limit 7")
                    ).all():
                        trivia.questions.append(question)

            db.session.add(trivia)
            db.session.commit()
        except Exception as exc:
            db.session.rollback()
            raise exc
            return render_error('Error occurred')

        return render_resource(trivia)
