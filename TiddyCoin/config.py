import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    secret_key = "358901v1395m1v31v159381y5u81y53185"