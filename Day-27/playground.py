#unlimited args with *

def add_m(*args):
   return sum(n for n in args)

test = add_m(1,2,3,4)


# create unlimited keyword arguments
# kwargs is a dictionary

def calc(n, **kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key)
        print(value)
    n+=kwargs["add"]
    n*= kwargs["multiply"]


## 
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make = "Toyota", model = "Land Cruiser")

print(my_car.model)
print(my_car.make)
