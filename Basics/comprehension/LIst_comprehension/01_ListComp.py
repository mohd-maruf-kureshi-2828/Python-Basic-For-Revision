"""
1 Approach
List1=list(range(0,101,2))
print(List1)
"""

"""
2 Approach
List2=[]
for i in range(0,101,2):
    List2.append(i)

print(List2)
"""

"""
# list Comprehension
List_com=[n for n in range(0,101,2)]
print(List_com)

"""
"""
# square find
sqr=[num**2 for num in range(1,6)]
print(sqr)
"""

"""
# Multiply Each Element by 2
mul=[num*2 for num in range(1,6)]
print(mul)

"""

"""
number=[10,20,30,40,50]
x=[num for num in number if num %4 == 0 ]
print(x) 

"""

"""
# Add 5 to Every Element
num=[1,2,3,4,5,6,7,8,9,10]
n=[n+5 for n in num ]
print(n)

"""

"""
# Convert String to Uppercase
std=['maruf','kureshi','umail','arbaz']
upperStd=[name.upper() for name in std]
print(upperStd)

"""

"""
# Filter Even Numbers from Range
even_number=[num for num in range(1,101) if num%2==0]
print(even_number)

"""

"""
# Nested List Comprehension
List=[[j for j in range(0,3)]for i in range(0,5)]
print(List)

"""