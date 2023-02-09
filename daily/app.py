class Car:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        pass
    
    def drive(self):
        print("the car is driving")
    
c1 = Car("ford", "f150")
print(c1)

class ElectricCar(Car):
    def __init__(self, make, model) -> None:
        super().__init__(make, model)
#---------------------------------------------------------

