
class Car:

    dealer_name = "lucky cars"
    cars_in_showroom = 0

    def __init__(self,model,name,for_sale):
        self.model = model
        self.name = name
        self.for_sale = for_sale
        Car.cars_in_showroom += 1

    def drive(self):
        print(f"you are driving a {self.name}.")

    def stop(self):
        print(f"{self.name} is stopping.")

    def describe(self):
        print(f"{self.model} {self.name}")