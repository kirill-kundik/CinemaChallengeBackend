from functools import wraps

from flask import request
from google.auth.transport import requests
from google.oauth2 import id_token

from repositories import UserRepository
from server import server
from util import render_error


def with_auth(method):
    @wraps(method)
    def auth_wrapper(*args, **kwargs):
        try:
            auth_header = request.headers['Authorization']
            token = auth_header.split(' ')[1]
            id_info = id_token.verify_oauth2_token(
                token, requests.Request(), server.config['GOOGLE_OAUTH_CLIENT_ID']
            )
            oid = id_info["sub"]
            picture = id_info["picture"]
            name = id_info["name"]
            email = id_info["email"]
            user = UserRepository.get(oid)
            if user:
                user = UserRepository.update(
                    oid, email, picture, name
                )
            else:
                user = UserRepository.create(
                    oid, email, picture, name
                )

            kwargs.update({'user': user})
            return method(*args, **kwargs)

        except Exception as exc:
            return render_error(str(exc), 401)

    return auth_wrapper
