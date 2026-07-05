def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done with {func.__name__}")
        return result
    return wrapper

@announce
def make_coffee():
    print("Brewing a coffee")

make_coffee()