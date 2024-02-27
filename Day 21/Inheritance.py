## Talking about inheritance
# 

class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe (self):
        print("inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__() # Super().__init__ allows us to inhereit all the attributes and methods from the Animal Class defined above

    def breathe(self):
        super().breathe() # this allows us to take the method breathe from the super class animal and then modify
        print("doing it under water")

    def swim(self):
        print("moving in water")


nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# What if I wanted to inherit a method but modify it a little bit