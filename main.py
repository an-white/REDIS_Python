from datetime import date
import random
import json

import redis

r = redis.Redis()

"""
    basic redis notes and commands
"""

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

## add a list of object to memory deprecate
random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": {
            "juan": "cabalo",
            "b": [1, 3, 2],
            "obj": {
                "mierda": 1
            }
        },
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
## add a list of object to memory deprecate


# add object in memory with json.dumps()
nested_obj = {'color': 'black',
              'price': 49.99,
              'style': 'fitted',
              "lista": [1, 2, 3],
              'quantity': {
                  'juan': 'cabalo',
                  'b': [1, 3, 2],
                  'obj': {
                      'mierda': 1
                  }
              },
              'npurchased': 0}

json_nested_obj = json.dumps(nested_obj)
r.set('nested', json_nested_obj)
r.get("nested")

item_list = [1, '2', 4]
json_items = json.dumps(item_list)
r.set("items", json_items)
r.get("items")
