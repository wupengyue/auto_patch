import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

pymysql.install_as_MySQLdb()
basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = "{{secret_key}}"

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'mysql://yueyue:Shanghai%40123@139.196.254.198:8306/luckyframe'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
