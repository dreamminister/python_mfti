import time
from functools import wraps

def timer(func):
    """Calculates time consumed by decorated function"""
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Elapsed: {}".format(time.time() - start))
        return result

    return wrapped

@timer
def operation(options):
    #print('start')
    time.sleep(1)
    #print('end')
    return options
