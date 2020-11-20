"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import achievements

ACHIEVEMENT_BLUEPRINT = Blueprint("achievement", __name__)

api = Api(ACHIEVEMENT_BLUEPRINT)
api.add_resource(achievements.AchievementsResources, "/achievements/<int:achievement_id>")
api.add_resource(achievements.AchievementResources, "/achievements")
api.add_resource(achievements.QuestionResources, "/achievements/<int:achievement_id>/questions")
