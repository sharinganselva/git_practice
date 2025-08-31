import functools
import time
from my_logger import logging


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: calling {func.__name__} with {args}, {kwargs} ")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} returned {result}")
        return result
    return wrapper


def retry(no_of_retries=5, wait=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, no_of_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print("fAttempt  # : {attempt}")
                    time.sleep(wait)
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator


def retry_test(no_of_retries=5, wait_for=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(0, no_of_retries):
                try:
                    no_of_retries -= 1
                    return func(args, kwargs)
                except Exception as e:
                    print(f"Attempt: #{attempt}")
                    time.sleep(wait_for)
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator


def time_taken_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"LOG: {func.__name__} took {elapsed_time} seconds")
        return result
    return wrapper
