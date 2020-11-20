""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(oid):
        """ Query a user by last and first name """
        return User.query.filter_by(oid=oid).one()

    @staticmethod
    def update(oid, email, profile_pic, name):
        """ Update a user's age """
        user = UserRepository.get(oid)
        user.email = email
        user.profile_pic = profile_pic
        user.name = name

        return user.save()

    @staticmethod
    def create(oid, email, profile_pic, name):
        """ Create a new user """
        user = User(
            oid=oid, email=email, profile_pic=profile_pic, name=name
        )

        return user.save()
