import redis
from config import REDIS_HOST, REDIS_PORT

redis_helper = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)