# Polymorphism
# Polymorphism allows for using a single interface for different types. In Python, polymorphism is implemented through method overriding.

class ElectricCar(Car):
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model} is silently starting...")

# Creating objects
car1 = Car('Toyota', 'Corolla', 2020)
car2 = ElectricCar('Tesla', 'Model 3', 2022, 75)

# Polymorphic behavior (same method name, different behavior)
car1.start_engine()  # Standard engine
car2.start_engine()  # Silent electric engine



# Inheritance
# Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class).

class ElectricCar(Car):  # Inheriting from Car class
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  # Calling the parent constructor
        self.battery_size = battery_size
    
    def charge_battery(self):
        print(f"The {self.model} is charging the battery...")

# Creating an instance of ElectricCar
my_electric_car = ElectricCar('Tesla', 'Model 3', 2022, 75)
my_electric_car.start_engine()
my_electric_car.charge_battery()



# Encapsulation
# Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data within a class and restricting access to some of the class’s components.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._engine_status = "off"  # Protected attribute
    
    def start_engine(self):
        self._engine_status = "on"
        print(f"Engine started for {self.make} {self.model}")
    
    def stop_engine(self):
        self._engine_status = "off"
        print(f"Engine stopped for {self.make} {self.model}")
    
    def get_engine_status(self):
        return self._engine_status

my_car = Car("Honda", "Civic", 2020)
my_car.start_engine()
print(my_car.get_engine_status())  # Accessing protected attribute through method




