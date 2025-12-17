"""
set methods- assignment
 1. take an empty set
 2. insert 5e lements from keyboard
 3. ask user to enter an element from keyboard,and delete that element from set
 4. ask user to enter an element from keyboard and print the position of that 
element
"""
empty=set()

print("Enter 5 Elements: ")
for i in range(5):
    element=int(input("Enter 5 Element : "))
    empty.add(element)
print("\nSet Elements Are :",empty)

del_element=int(input("Enter Element To Dlete : "))
if del_element in empty:
    empty.remove(del_element)
    print("Element Delete Successfully")
else:
    print("Element not found in set")


print("Updated Set:",empty)

search_element=int(input("Enter A Element To Find Position : "))

temp_list=list(empty)
if search_element in temp_list:
    position=temp_list.index(search_element)
    print(f'elemet find on this Position {position}')
