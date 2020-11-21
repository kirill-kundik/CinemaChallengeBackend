"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import trivias

TRIVIA_BLUEPRINT = Blueprint("trivia", __name__)

api = Api(TRIVIA_BLUEPRINT)

api.add_resource(trivias.TriviasResources, "/trivia")
api.add_resource(trivias.TriviaResources, "/trivia/<int:trivia_id>")
api.add_resource(trivias.SubmitAnswerResources, "/trivia/<int:trivia_id>/submitAnswer")
