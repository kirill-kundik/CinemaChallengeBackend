"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import users

USER_BLUEPRINT = Blueprint("user", __name__)

api = Api(USER_BLUEPRINT)
api.add_resource(users.UserResources, "/users/<string:oid>")
api.add_resource(users.UsersResources, "/users")
api.add_resource(users.UserObtainResources, "/users/<string:oid>/obtain")
