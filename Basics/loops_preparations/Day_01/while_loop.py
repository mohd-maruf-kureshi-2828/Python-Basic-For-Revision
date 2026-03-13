#while loop
#while condition:
#    code to execute
#Example
"""
i = 1
while i < 5: # while loop will run until the condition is true
    print(i)
    i += 1 # incrementing the value of i by 1 in each iteration
"""

"""
Q1: print numbers from 5 to 1 using while loop
i=5
while i>=1:
    print(i, end=" ")
    i-=1 # decrementing the value of i by 1 in each iteration
"""

"""
Q2: print the sum of numbers from 1 to 10 using while loop
i=1
sum=0
while i<=10:
    sum += i
    i+= 1
print(sum)
"""

"""
# Q3: count the number of digits in a given number using while loop
number = int(input("Enter a number: "))
count = 0
while number > 0:
    number //= 10 # number = number // 10, this will remove the last digit of the number
    count += 1
print(f"The number of digits in the given number is: {count}")
"""

# Q4: Reverse a given number using while loop
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    digit = number % 10 # this will give the last digit of the number
    reverse = reverse * 10 + digit # this will add the last digit to the reverse number
    number //= 10 # this will remove the last digit of the number
print(f"The reverse of the given number is: {reverse}")