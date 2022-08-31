from unittest.main import MODULE_EXAMPLES


class Car:

    def __init__(self, type, brand, model, num_passengers, fuel_amount):
        self.type = type
        self.brand = brand
        self.model = model
        self.num_passengers = num_passengers
        self.fuel_amount = fuel_amount
    
    def __str__(self):
        return f"{self.brand} {self.model} with {self.num_passengers} passengers and {self.fuel_amount} gallons of fuel"
    
    def drive(self, A, B):
        print(f"{self.__str__()} drives from {A} to {B}")
    
    def refuel(self, num_gallons):
        self.fuel_amount += num_gallons
        print(f"{self.brand} {self.model} now has {self.fuel_amount} gallons of gas.")
    
bugatti = Car("Racecar", "Bugatti", "Veyron", 69, 24)
print(bugatti)
bugatti.refuel(23)
bugatti.drive("cliff", "bottom of cliff")