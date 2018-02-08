from functools import wraps

def transform(transform_func):
    """Transforms return result from decorated functions"""
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform_func(result)
        return wrapped
    return decorator

@transform(str.upper)
def reverse_word(text):
    """Reverse letter order in the word"""
    if type(text) is not str:
        text = str(text)
    return text[::-1]
