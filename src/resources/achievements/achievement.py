"""
Define the REST verbs relative to the users
"""

from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import AchievementRepository
from util import render_resource, parse_params


class AchievementResources(Resource):
    """ Verbs relative to the users """

    @staticmethod
    def get(**_kwargs):
        """ Return an user key information based on his name """
        return render_resource(AchievementRepository.all())

    @staticmethod
    @parse_params(
        Argument("name", required=True, help="Name of the achievement", location="json"),
        Argument("short_description", required=True, help="Short description of the achievement", location="json"),
        Argument("long_description", required=True, help="Long description of the achievement", location="json"),
        Argument("difficulty", required=True, type=int, help="Difficulty of the achievement", location="json"),
        Argument("image_src", required=True, help="Image of the achievement", location="json"),
        Argument("bg_image_src", required=True, help="Bg image of the achievement", location="json"),
    )
    def post(name, short_description, long_description, difficulty, image_src, bg_image_src, **_kwargs):
        return render_resource(AchievementRepository.create(
            name,
            short_description,
            long_description,
            difficulty,
            image_src,
            bg_image_src
        ))

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
