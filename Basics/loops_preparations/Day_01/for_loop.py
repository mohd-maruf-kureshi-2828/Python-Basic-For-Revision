"""
Q1: print numbers 1 to 5
print numbers 1 to 5
for i in range(1,6):
    print(i)
"""

"""
Q2: print numbers 10 to 1
for i in range(10,0,-1): start from 10, end at 1, step -1
    print(i)
"""

"""
Q3: print even and odd numbers from 1 to 100
for i in range(1,100): start from 1, end at 100
    if i % 2 == 0: # if the number is divisible by 2, it is even
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
"""


"""
Q4: print the squares of numbers from 1 to 5
for i in range(1, 6):
    print(f'{i*i} is the square of {i}') square of a number is the number multiplied by itself
"""

"""
Q5: print the multiplication table of a number entered by the user
userNumber=int(input("Enter a number to print a table: "))
for i in range(1,11):
    print(f"{userNumber} X {i} = {userNumber*i}")
"""

"""
Q6: print the sum of numbers from 1 to 10
sum=0
for i in range(1, 11):
    sum += i # sum = sum + i sum zero se start hoga aur har iteration me i ko sum me add karega
print(f"The sum of numbers from 1 to 10 is {sum}")
"""

"""
Q7: print the factorial of a number entered by the user

# factorial kya hota hai? factorial ek number ka product hota hai uske saare positive integers ke saath. jaise 5! = 5 x 4 x 3 x 2 x 1 = 120

userFactorial=int(input("Enter a number to find its factorial: ")) 
fact = 1

for i in range(1, userFactorial + 1): # start from 1, end at userFactorial, step 1
    fact *= i # fact = fact * i
print(f"The factorial of {userFactorial} is {fact}")
"""

"""
Q8: count the number of vowels in a given text

text="python programming is fun"
count=0
for i in text:
    if i in "aeiou": # check if the character is a vowel
        count += 1 # count = count + 1 
       
print(f"The number of vowels in the text is {count}") 
# output: The number of vowels in the text is 6
"""

"""
Q9: print the characters of a string entered by the user one by one
userStr=input("Enter a character to print: ")
for i in userStr:
    print(i)
"""

"""
Q10: print a pattern of stars
for i in range(1, 6):
    print('*'*i)
"""