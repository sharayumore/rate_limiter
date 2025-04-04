import redis

# Connect to local Redis or Render's Redis URL
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)