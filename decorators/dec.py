import time

def delay_dec(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


# basically uses delay_dec to inject more behavior into a function
@delay_dec
def say_hello():
    print("Hello")

    
say_hello()
