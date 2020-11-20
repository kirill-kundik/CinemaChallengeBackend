""" Defines the User repository """

from models import Achievement


class AchievementRepository:
    """ The repository for the user model """

    @staticmethod
    def get(id_):
        """ Query a user by last and first name """
        return Achievement.query.filter_by(id=id_).one_or_none()

    @staticmethod
    def all():
        return Achievement.query.all()

    @staticmethod
    def update(
            id_, name, short_description, long_description, difficulty, image_src, bg_image_src
    ):
        """ Update a user's age """
        achievement = AchievementRepository.get(id_)
        achievement.name = name or achievement.name
        achievement.short_description = short_description or achievement.short_description
        achievement.long_description = long_description or achievement.long_description
        achievement.difficulty = difficulty or achievement.difficulty
        achievement.image_src = image_src or achievement.image_src
        achievement.bg_image_src = bg_image_src or achievement.bg_image_src

        return achievement.save()

    @staticmethod
    def create(name, short_description, long_description, difficulty, image_src, bg_image_src):
        """ Create a new user """
        achievement = Achievement(
            name=name, short_description=short_description, long_description=long_description,
            difficulty=difficulty, image_src=image_src, bg_image_src=bg_image_src
        )

        return achievement.save()
