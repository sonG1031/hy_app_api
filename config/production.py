from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'hy.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'1\xf5\x13I:\xeb\xde\xf6\xdf^6\xd7\x00`\xe4\x7f'