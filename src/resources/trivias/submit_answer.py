"""
Define the REST verbs relative to the users
"""

from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import SubmittedAnswer, Trivia
from repositories import AchievementRepository, UserRepository
from services import with_auth
from util import parse_params, render_resource


class SubmitAnswerResources(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @parse_params(
        Argument("answer_id", location="json", type=int, required=True, help="Answer id"),
    )
    @with_auth
    def post(answer_id, trivia_id, user, **_kwargs):
        """ Return an user key information based on his name """
        answer = SubmittedAnswer(answer_id=answer_id, trivia_id=trivia_id, user_id=user.oid).save()
        trivia = Trivia.query.filter_by(id=trivia_id).one()
        achievement = AchievementRepository.get(trivia.achievement_id)

        if len(trivia.submitted_answers) == len(achievement.questions):
            achieved = True

            for answer in trivia.submitted_answers:
                if not answer.answer.is_right:
                    achieved = False
                    break

            if achieved:
                UserRepository.obtain(user, achievement)

        return render_resource(answer)
