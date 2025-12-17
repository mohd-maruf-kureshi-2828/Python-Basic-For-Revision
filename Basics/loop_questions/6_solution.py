number=int(input("Enter A Number To Check Its Factorial : "))
factory_num=1
"""
factorial of 5
5 * 4 * 3 * 2 * 1
""" 

while number >= 1:
    """
    factory_num = factory_num * number
    number = number - 1
    
    """
    factory_num *= number
    number -= 1

print("Your Number Factories Values Is : ",factory_num)