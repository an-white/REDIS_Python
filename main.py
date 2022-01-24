from datetime import date
import random

import redis

r = redis.Redis()

# set the object to save in memory
r.mset({"prop": "kazaz"})

# get a value from key
r.get("prop")

today = date.today().isoformat()
visits = {"carlos", "karla", "pedro"}
# add a set of values my init today value is "2022-01-24"
r.sadd(today, *visits)

# get values of the set
r.smembers(today)

# get set length
r.scard(today)

## add a list of object to memory
random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
        }

with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        # TODO find a no deprecate function to store dict in REDIS
        pipe.hmset(h_id, hat)
    pipe.execute()

r.bgsave()

a = [10, 20, None, 12]
newA = list(filter(lambda y: y < 20, filter(lambda x: x > 10 if x else False, a)))
