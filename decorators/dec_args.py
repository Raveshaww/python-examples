def shout(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}"

print(order("Burger", "Fries"))