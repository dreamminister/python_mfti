def coroutine(f):
    def wrap(*args,**kwargs):
        gen = f(*args,**kwargs)
        gen.send(None)
        return gen
    return wrap

@coroutine
def multiplier():
    counter = 1
    while True:
        user_input = (yield)
        result = counter * user_input
        print(result)
        counter += 1
