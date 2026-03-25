
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


# second example for bank account

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('invalid withdraw')

    def getBalace(self):
        return self.__balance
    
kumar=BankAccount(1200)
print('after withdraw',kumar.getBalace())
kumar.withdraw(500)
print('before withdraw',kumar.getBalace())
kumar.deposit(500)
print('before deposit',kumar.getBalace())

# kumar.deposit(100)
