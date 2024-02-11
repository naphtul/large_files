import time
from os import stat

import humanize


def get_file_size(file_name: str) -> str:
    return humanize.naturalsize(stat(file_name).st_size)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds to complete.")
        return result

    return wrapper
