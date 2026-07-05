# Implement a decorator called no_duplicates
# If a function is called with the same arguments more than one dont execute 

seen = set()

def no_duplicates(func):
    def wrapper(*args, **kwargs):
        if args in seen:
            print("Duplicate call detected")
        else:
            seen.add(args)
            result = func(*args, **kwargs)
            return result
    return wrapper

@no_duplicates
def greet(name):
    print(f"Hello {name}")

greet("Ethan")
greet("Ethan")
greet("Bob")
greet("Ethan")