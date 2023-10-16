# decorators are the functions which helps tp change and retuen functions it takes and update and return the unction
''' syntax
decorator_function
 def my_function():
     pass
'''


def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx
@greet
def add(a,b):
    print(a+b)

@greet
def hello():
    print("hello world")
hello()
add(1,2)


import logging

def log_function_call(func):
    def decorated(*args,**kwargs):
        logging.info(f"calling{func.__name__} with args={args},kwargs={kwargs}")
        result = func(*args,**kwargs)
        logging.info(f"{func.__name__} returned{result}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b

my_function(1,4)
