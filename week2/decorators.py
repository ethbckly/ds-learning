# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"
say_hi = greet
print(say_hi("Alex"))

# Passing a function as an argument
def apply(f, v):
    return(f(v))
res = apply(say_hi, "Eth")
print(res)

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))

# Higher order functions

def fun(f, x):
    return f(x)

def square(x):
    return x * x
res = fun(square, 5)
print(res)

# Types of Decorators -------------------------------------------------

# Function decorators - Used to wrap and enhance functions by adding extra behaviour before or after
def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@simple_decorator
def greet():
    print("Hello World")
greet()

# Method Decorators - Special decorators used for methods inside a class handling self parameters

def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

# Class decorators - Used to modify or enhance behaviour of a class

def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass
print(Person.class_name)

# Built-in Decorators
# @staticmethod - defines a method that does not operate on an instance of class

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
res = MathOperations.add(5, 3)
print(res)

# @classmethod - defines a method that operates on class itself
class Employee:
    raise_amount = 1.05
    def __int__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

Employee.set_raise_amount(1.10)
print(Employee.raise_amount)