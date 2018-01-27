# url: https://www.coursera.org/learn/programming-in-python/programming/0664k/diekorator-to-json

from functools import wraps
import json

def to_json(func):
    
    @wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        json_result = json.dumps(result)
        return json_result

    return wrapped


@to_json
def get_data():
      return { 'data': 42, 'garbage' : [1, "text"], 'map': {1:['one'] }}

print(get_data.__name__)

result = get_data()
print(result)