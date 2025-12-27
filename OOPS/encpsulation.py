
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self): #encapsulation
        return self.__brand
    
    def fullName(self):
        print(f'brand is {self.__brand} model is {self.model}')

    
my_sec=Car('Toyata','Fortuner')
print(my_sec.get_brand())