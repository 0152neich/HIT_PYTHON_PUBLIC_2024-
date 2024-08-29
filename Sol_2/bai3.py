class Vehicle:
    def __init__(self, make: str):
        self.make = make
    
    def description(self) -> str:
        return f"Vehicle make: {self.make}"

class Car(Vehicle):
    def __init__(self, make: str, model: str):
        super().__init__(make)
        self.model = model
    
    def description(self) -> str:
        return f"Car make: {self.make}, model: {self.model}"

class ElectricCar(Car):
    def __init__(self, make: str, model: str, battery_size: float):
        super().__init__(make, model)
        self.battery_size = battery_size
    
    def description(self) -> str:
        return f"Electric Car make: {self.make}, model: {self.model}, battery size: {self.battery_size} kWh"

vehicle = Vehicle("Toyota")
car = Car("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model S", 100)

print(vehicle.description())
print(car.description())
print(electric_car.description())
