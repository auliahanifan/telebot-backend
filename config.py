import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('DB_PORT', '3306'))
DB_DATABASE = os.environ.get('DB_DATABASE', 'telegram_bot')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'workshop')


IS_PRODUCTION = str(os.environ.get('IS_PRODUCTION', 'false')).lower() == 'true'
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', 'http://localhost')
