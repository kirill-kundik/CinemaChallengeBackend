"""
Define the REST verbs relative to the users
"""

import sqlalchemy
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
        Argument("question_id", location="json", type=int, required=True, help="Question id"),
    )
    @with_auth
    def post(answer_id, trivia_id, question_id, user, **_kwargs):
        """ Return an user key information based on his name """
        answer = SubmittedAnswer(
            answer_id=answer_id, trivia_id=trivia_id, user_id=user.oid, question_id=question_id
        ).save()
        trivia = Trivia.query.filter_by(id=trivia_id).one()
        achievement = AchievementRepository.get(trivia.achievement_id)

        if achievement:
            if len(trivia.submitted_answers) == len(achievement.questions):
                trivia.completed = True
                trivia.save()
                achieved = True

                for answer in trivia.submitted_answers:
                    if not answer.answer.is_right:
                        achieved = False
                        break

                if achieved:
                    user.achievements_rate = user.achievements_rate + 50
                    user.save()
                    try:
                        UserRepository.obtain(user, achievement)
                    except sqlalchemy.orm.exc.FlushError:
                        pass
        elif len(trivia.submitted_answers) == len(trivia.questions) * 2:
            trivia.completed = True
            trivia.save()

            players_score = {trivia.user_id: 0, trivia.second_player_id: 0}

            for answer in trivia.submitted_answers:
                for aanswer in trivia.submitted_answers:
                    if aanswer.id == answer.id:
                        continue
                    if aanswer.question_id != answer.question_id:
                        continue
                    if aanswer.answer.is_right and answer.answer.is_right:
                        if aanswer.created_at < answer.created_at:
                            players_score[aanswer.user_id] += 1
                        else:
                            players_score[answer.user_id] += 1
                    elif aanswer.answer.is_right:
                        players_score[aanswer.user_id] += 1
                    elif answer.answer.is_right:
                        players_score[answer.user_id] += 1

            print(players_score)

            first_player_id, first_player_score = players_score.popitem()
            second_player_id, second_player_score = players_score.popitem()

            if first_player_score == second_player_score:
                user = UserRepository.get(first_player_id)
                user.trivia_rate = user.trivia_rate + 20
                user.save()

                user = UserRepository.get(second_player_id)
                user.trivia_rate = user.trivia_rate + 20
                user.save()

                trivia.first_player_score = 20
                trivia.second_player_score = 20
                trivia.save()
            elif first_player_score > second_player_score:
                user = UserRepository.get(first_player_id)
                user.trivia_rate = user.trivia_rate + 45
                user.save()

                trivia.first_player_score = 45
                trivia.second_player_score = 0
                trivia.save()
            else:
                user = UserRepository.get(second_player_id)
                user.trivia_rate = user.trivia_rate + 45
                user.save()

                trivia.first_player_score = 0
                trivia.second_player_score = 45
                trivia.save()

        return render_resource(answer)
