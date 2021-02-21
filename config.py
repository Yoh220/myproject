import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'y2434kgkfdl55lsdlf'
