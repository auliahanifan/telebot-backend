import os
from dotenv import load_dotenv

load_dotenv()

# Telebot
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Redis
REDIS_HOST = os.environ.get('REDIST_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))

# Database
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_USER = os.environ.get('DB_USER', 'app_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'app_user')
