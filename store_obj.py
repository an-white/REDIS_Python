from redis.cluster import RedisCluster as Redis

rc = Redis(host='localhost', port=6379)
