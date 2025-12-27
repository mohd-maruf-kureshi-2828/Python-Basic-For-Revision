class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Battery:
    def battery_info(self):
        return'this is battery'

class Engine:
    def engine_info(self):
        return'this is engine'

class ElectricCar(Battery,Engine,Car):
    pass

my_new_tesla=ElectricCar('tesla','model s')
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())