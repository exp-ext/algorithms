from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        time_end = time()
        print(
            f'\nФункция: {f.__name__}\n'
            f'args & kwargs:[{args}, {kwargs}]\n'
            f'отработала за {time_end-time_start} сек\n'
            '------------------------------------------'
        )
        return result
    return wrap
