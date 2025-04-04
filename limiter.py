import time
from redis_client import redis_client

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    def is_allowed(self, user_id):
        key = f"rate_limit:{user_id}"
        current_time = int(time.time())

        # Start of the window
        window_start = current_time - self.window_seconds

        # Remove outdated timestamps
        redis_client.zremrangebyscore(key, 0, window_start)

        # Count remaining
        current_count = redis_client.zcard(key)

        if current_count < self.max_requests:
            # Add new timestamp
            redis_client.zadd(key, {current_time: current_time})
            redis_client.expire(key, self.window_seconds)
            return True
        return False