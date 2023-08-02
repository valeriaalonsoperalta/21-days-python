class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model 
        self.year = year 
        self.mileage = mileage
        self.state = False


    def turnOn(self):
        self.state = True
    def turnOff(self):
        self.state = False
    def drive(self,km):
        if (self.state):
            self.mileage = self.mileage + km 
        else:
            raise Exception("El auto está apagado")
            
            
    



toyota = Car("Toyota", "Corolla", 2020, 0)
toyota.drive(200)
print(toyota.mileage)


