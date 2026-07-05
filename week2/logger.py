# Implement a logger decorator that when applied to the function prints the function name before and after

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")

        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello {name}")

greet("Ethan")