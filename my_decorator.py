import time


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
