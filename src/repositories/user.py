""" Defines the User repository """

from models import User, Obtained


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(oid):
        """ Query a user by last and first name """
        return User.query.filter_by(oid=oid).one_or_none()

    @staticmethod
    def update(oid, email, profile_pic, name):
        """ Update a user's age """
        user = UserRepository.get(oid)
        user.email = email or user.email
        user.profile_pic = profile_pic or user.profile_pic
        user.name = name or user.name

        return user.save()

    @staticmethod
    def create(oid, email, profile_pic, name):
        """ Create a new user """
        user = User(
            oid=oid, email=email, profile_pic=profile_pic, name=name
        )

        return user.save()

    @staticmethod
    def obtain(user, achievement):
        user.achievements.append(Obtained(achievement=achievement))

        return user.save()
