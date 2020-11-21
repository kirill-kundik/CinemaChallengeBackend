"""
Define the REST verbs relative to the users
"""

from flask_restful import Resource

from models import Trivia
from services import with_auth
from util import render_resource, render_error


class TriviaResources(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @with_auth
    def get(trivia_id, user, **_kwargs):
        """ Return an user key information based on his name """
        trivia = Trivia.query.filter_by(id=trivia_id).one_or_none()
        if trivia:
            if trivia.user_id != user.id and trivia.second_player_id != user.id:
                return render_error('You are not authorized to access this page', 401)
        return render_resource(trivia)
