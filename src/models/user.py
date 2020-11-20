"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "user"

    oid = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    profile_pic = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    achievements = db.relationship("Obtained", back_populates="user")

    def __init__(self, oid, email, profile_pic, name):
        """ Create a new User """
        self.oid = oid
        self.email = email
        self.profile_pic = profile_pic
        self.name = name

    def get_id(self):
        return self.oid
