from functools import wraps

def Override(info=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            class_name = args[0].__class__.__name__ if args else 'UnknownClass'
            method_name = func.__name__
            print(f"Calling {class_name}.{method_name} with args={args[1:]} and kwargs={kwargs} - Info: {info}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
