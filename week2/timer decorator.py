import time

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()
        print(after - before)
        return result
    return wrapper

@timer
def slow():
    time.sleep(2)

slow()

@timer
def add(a, b):
    return a+b

print(add(3, 4))