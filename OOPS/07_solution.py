class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car += 1
    

    def get_brand(self): #encapsulation
        return self.__brand
    
    def fullName(self):
        print(f'brand is {self.__brand} model is {self.model}')

    @staticmethod
    def general_description():
        return 'Cars Are Amazing'
    
myCar=Car('Toyata','siera')
# print(myCar.general_description())
print(Car.general_description())