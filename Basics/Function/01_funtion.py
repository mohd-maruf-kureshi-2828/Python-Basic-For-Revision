def names():
    print("maruf")
    print("arbaz")
    print("umair")

# names()

# funtion with parameters
def add(num1,num2):
    print(num1+num2)

# add(10,10)

# asignment 
def findBigNumber(num1,num2,num3):
    if num1 >=num2 and num1 >=num3:
        print(f'{num1} is greater then {num2} and {num3}')
    elif num2 >= num1 and num2>=num3:
        print(f'{num2} is greater then {num1} and {num3}')
    else:
         print(f'{num3} is greater then {num1} and {num2}')

# findBigNumber(10,20,5)
