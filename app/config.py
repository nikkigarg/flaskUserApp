import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = "1asdfghjklvcxzxcvbnmlhgwqwertyuiofdfgh"  # os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{pw}@{url}/{db}'.format(user="postgres", pw="password",
                                                                         url="127.0.0.1:5432",
                                                                         db="FlaskUM")  # os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT: 465
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = "usrgmail@gmail.com" # privde ur email and password here
    MAIL_PASSWORD = "urPassword"
