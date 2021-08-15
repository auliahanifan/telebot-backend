import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
REDIS_HOST = os.environ.get('REDIST_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))