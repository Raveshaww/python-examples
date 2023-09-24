from functools import wraps

def dec(function):
    # Ensures that the decorator doesn't strip the function of any documentation
    @wraps(function)
    def wrapper(*args, **kwargs):
        """# I am in the wrapper function"""
        function(*args, **kwargs).upper()
    return wrapper


@dec
def hi():
    """says hi"""
    return "Hi"

hi()