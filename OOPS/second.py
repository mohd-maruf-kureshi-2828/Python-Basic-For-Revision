"""
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_car=Car('Toyata','corolla')
print(my_car.brand)
print(my_car.model)

my_frd=Car('tata','nexon')
print(my_frd.brand)
print(my_frd.model)

"""

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self): #encapsulation
        return self.__brand
    
    def fullName(self):
        print(f'brand is {self.__brand} model is {self.model}')

    
my_sec=Car('Toyata','Fortuner')
# print(my_sec.get_brand())
# my_sec.fullName()



class ElecticCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
my_electric=ElecticCar('Tesla','model s','86kwh')
print(isinstance(my_electric,Car))
print(isinstance(my_electric,ElecticCar))

# print(my_electric.model)
# my_electric.fullName()