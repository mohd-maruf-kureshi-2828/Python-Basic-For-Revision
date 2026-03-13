"""
arithematic operators
comparison operators
logic operator 
assignment operator
member operator
identity operator
"""
# arithematic operators
# arthematic operators are used to perform mathematical operations on numbers.
a = 10
b = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b)  # exponentiation

# comparison operators
# comparison operators are used to compare two values and return a boolean result.
x = 10
y = 5
print(x > y)  # greater than
print(x < y)  # less than
print(x == y)  # equal to
print(x != y)  # not equal to
print(x >= y)  # greater than or equal to
print(x <= y)  # less than or equal to

# logic operator
# logic operators are used to combine multiple boolean expressions and return a boolean result.
p = True
q = False
print(p and q)  # logical AND
print(p or q)  # logical OR
print(not p)  # logical NOT

# assignment operator
# assignment operators are used to assign values to variables.
c = 10
c += 5  # equivalent to c = c + 5
print(c)
c -= 3  # equivalent to c = c - 3
print(c)
c *= 2  # equivalent to c = c * 2
print(c)

# member operator
# member operators are used to check if a value is present in a sequence (like a list, tuple, or string).
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
my_string = "Hello, World!"
print("Hello" in my_string)  # True
print("Python" in my_string)  # False

# identity operator
# identity operators are used to compare the memory locations of two objects.
a = [1, 2, 3]
b = a  # b references the same list as a
print(a is b)  # True
c = [1, 2, 3]  # c is a different list with the same content
print(a is c)  # False
print(a == c)  # True, because they have the same content
