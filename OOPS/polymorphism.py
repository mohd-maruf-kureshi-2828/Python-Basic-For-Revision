class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return 'dieser or petrol'
    
NonBatery=Car('Tata','Safari')
print(NonBatery.fuel_type())

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return 'battery charge'
    
BatteryCar=ElectricCar('Tesla','model s','85wh')
print(BatteryCar.fuel_type())