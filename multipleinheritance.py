
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Prey(Animal):
    def flee(self):
        print("animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("animal is hunting")

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

fish = Fish("nemo")
fish.hunt()
fish.flee()
fish.eat()
