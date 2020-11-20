"""
Define the REST verbs relative to the users
"""
import sqlalchemy
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from repositories.achievement import AchievementRepository
from services import with_auth
from util import render_resource, parse_params, render_error


class UserObtainResources(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @with_auth
    def get(oid, user, **_kwargs):
        return render_resource(user.achievements)

    @staticmethod
    @parse_params(
        Argument("achievement_id", type=int, location="json", required=True, help="The age of the user.")
    )
    @with_auth
    def post(oid, user, achievement_id, **_kwargs):
        """ Return an user key information based on his name """
        achievement = AchievementRepository.get(achievement_id)
        if achievement:
            try:
                user = UserRepository.obtain(user, achievement)
            except sqlalchemy.orm.exc.FlushError:
                return render_error('User has already obtained this achievement')
        return render_resource(user)

    # @staticmethod
    # @parse_params(
    #     Argument("age", location="json", required=True, help="The age of the user.")
    # )
    # @swag_from("../swagger/user/POST.yml")
    # def post(last_name, first_name, age):
    #     """ Create an user based on the sent information """
    #     user = UserRepository.create(
    #         last_name=last_name, first_name=first_name, age=age
    #     )
    #     return jsonify({"user": user.json})
    #
    # @staticmethod
    # @parse_params(
    #     Argument("age", location="json", required=True, help="The age of the user.")
    # )
    # @swag_from("../swagger/user/PUT.yml")
    # def put(last_name, first_name, age):
    #     """ Update an user based on the sent information """
    #     repository = UserRepository()
    #     user = repository.update(last_name=last_name, first_name=first_name, age=age)
    #     return jsonify({"user": user.json})
