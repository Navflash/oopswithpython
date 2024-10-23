from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def drive(self):
        print("lets gooo")

    def stop(self):
        print("stopppppp")
    
    

vehicle = Car()
vehicle.drive()