import random

def bound_random(start, stop):
    space = list(range(min(start, stop+1), max(start, stop+1)))

    while len(space) > 0:
        result = random.choice(space)
        yield result
        space.remove(result)
