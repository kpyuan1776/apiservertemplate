import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/apiserverdb'
        SQLALCHEMY_DATABASE_URI = 'mysql://korbinian_paul_googlemail_com:apipassword@localhost/apiserverdb'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

        SECRET_KEY = os.environ.get('SECRET_KEY') or 'apiserver08042020'
        SECRET_REFRESH_KEY = os.environ.get('SECRET_REFRESH_KEY') or 'apiserverrefreshtoken'


