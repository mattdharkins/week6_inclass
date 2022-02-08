import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Set Config variables for the flask app.
    Using environment variables where available otherwise create
    the config variable if not done already.

    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess.'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
