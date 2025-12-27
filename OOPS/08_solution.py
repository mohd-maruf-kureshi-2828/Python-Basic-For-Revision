class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

        Car.total_car += 1
    

    def get_brand(self): #encapsulation
        return self.__brand
    
    def fullName(self):
        print(f'brand is {self.__brand} model is {self.__model}')

    @staticmethod
    def general_description():
        return 'Cars Are Amazing'
    
    @property
    def model(self):
        return self.__model
    
    
myCar=Car('Toyata','siera')
# myCar.model='Scorpio'
print(myCar.model)