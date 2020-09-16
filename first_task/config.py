import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://' \
                              f'{os.environ.get("PSQL_LOGIN")}:' \
                              f'{os.environ.get("PSQL_PASS")}@' \
                              f'{os.environ.get("PSQL_HOST")}/' \
                              f'{os.environ.get("TICKET_DB")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('TASK1_SECRET_KEY') or 'this is secret key'
