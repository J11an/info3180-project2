import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    DATABASE_URL='postgresql://sjidchjzuzcdej:cdd94ea48294fc1e539c6fea1a2ce823db30bb08dc967f3dee1323f9b2632647@ec2-3-209-124-113.compute-1.amazonaws.com:5432/d5hem1nrio7rbk'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed