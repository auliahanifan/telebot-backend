import redis
from config import *

redis_helper = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
