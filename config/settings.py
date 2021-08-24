from os import environ


POSTGRES = {
    'user': environ.get('POSTGRES_USER', 'auth_user_core'),
    'pw': environ.get('POSTGRES_PASS', 'qwerty123'),
    'db': environ.get('POSTGRES_DB', 'auth_db'),
    'host': environ.get('POSTGRES_HOST', 'localhost'),
    'port': environ.get('POSTGRES_PORT', '5432'),
}

MAIL = {
    'username': environ.get('EMAIL_USER'),
    'password': environ.get('EMAIL_PASSWORD'),
}

SMTP = {
    'host': environ.get('SMTP_HOST'),
    'port': environ.get('SMTP_PORT'),
}

UPLOAD_IMAGE = {
    'path': environ.get('UPLOAD_IMAGE_PATH'),
    'extensions': environ.get('UPLOAD_IMAGE_EXTENSIONS'),
}

SQLALCHEMY_DATABASE_URI = (
    'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
)
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False

REDIS_URI = 'localhost'
REDIS_DB = '10'

CDN_SERVER = {
    'ip': environ.get('CDN_SERVER_IP'),
    'port': environ.get('CDN_SERVER_PORT'),
    'user': environ.get('CDN_SERVER_USER'),
    'password': environ.get('CDN_SERVER_PASS'),
}

DEBUG = True

ABS_OD_URL = environ.get('ABS_OD_URL')
