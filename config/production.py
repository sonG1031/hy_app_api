from config.default import *
from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'1\xf5\x13I:\xeb\xde\xf6\xdf^6\xd7\x00`\xe4\x7f'