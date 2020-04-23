import os
from config import Config


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') \
                 or 'you-will-never-guess'
