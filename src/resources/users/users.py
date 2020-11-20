"""
Define the REST verbs relative to the users
"""

from flask_restful import Resource

from services import with_auth
from util import render_resource


class UsersResources(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @with_auth
    def get(user, **_kwargs):
        """ Return an user key information based on his name """
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
