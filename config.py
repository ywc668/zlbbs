import os


SECRET_KEY = os.urandom(24)

DEBUG = True


DB_USERNAME = 'root'
DB_PASSWORD = '0Stric4e$'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zlbbs'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'ASDF'

#PERMANENT_SESSION_LIFETIME =
