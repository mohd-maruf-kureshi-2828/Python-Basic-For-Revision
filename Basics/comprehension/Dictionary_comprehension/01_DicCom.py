"""
dic={x:x**2 for x in range(1,6)}
print(dic)

"""

"""
# Convert two lists into dictionary
keys = ['name', 'age', 'city','Role']
values = ['Maruf', 21, 'Bangalore','Full Stack']

my_dic={keys[i]:values[i] for i in range(len(keys))}
print(my_dic)
"""

"""
# Filtered Dictionary (Using Condition)
numbers = [1, 2, 3, 4, 5, 6]
find_even={i:i**2 for i in numbers if i % 2 == 0}
print(find_even)
"""

"""
# Convert String to Dictionary (Letter Count)
words='apple'
char_count={ch:words.count(ch) for ch in words}
print(char_count)

"""

"""
# Uppercase Key – Lowercase Value Dictionary
words = ['Python', 'AI', 'Code']
result={world.upper():world.lower() for world in words}
print(result)

"""


"""

# Reverse Key and Value
data = {'a': 10, 'b': 20, 'c': 30}
reversed_dic={key:value for key,value in data.items()}
print(reversed_dic)


"""


# Real-Life Example (For Interview or Project)
marks = {'Maruf': 80, 'Rahul': 45, 'Aman': 30}
result={key:('pass' if score>=40 else 'fail') for  key,score in marks.items()}

print(result)