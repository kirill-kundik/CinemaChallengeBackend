from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .achievement import Achievement
from .obtained import Obtained
from .question import Question
from .answer import Answer
from .trivia import Trivia
