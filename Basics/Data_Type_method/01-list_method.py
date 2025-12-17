# my_list=[10,20,30,40]
# my_list.append(50)
# print(my_list)
# print(my_list.count(400))
# my_list.pop()
# print(my_list)




"""


exploring list methods– assignment
 1. take an emptylist
 2. read and store 10 elements from keyboard and store in list
 3. print all list elements
 4. ask user to enter a position and element from the keyboard, and insert that
 element before that position
 5. askuser to enter an element to delete from the list, and delete that element
 if it is available
 6. ask user to enter a position, and delete that element from the list if that
 position is available
 7. ask user to enter an element and print the position of that element if
 available, else print-1

"""
empty=[]

print("Enter 10 Element :")
for i in range(10):
    element=int(input("Enter element : "))
    empty.append(element)

print(empty)


pos=int(input("Enter the position where u want to insert ! :"))
new_element=int(input("Enter the Element To Insert !"))
if 0<=pos<=len(empty):
    empty.insert(pos,new_element)
    print("ELement Inserted Succcessfully🎉")
    print(empty)
else:
    print("invalid position")

del_element=int(input("enter element to delete (by value): "))
if del_element in empty:
    empty.remove(del_element)
    print(f'Deleted Element Successfully🎉')
else:
    print('Element Not Found')

print("Updated List:", empty)

search_element=int(input('Enter element to search position : '))
if search_element in empty:
    position=empty.index(search_element)
    print(f'Element found at position {position}')
else:
    print("Element Not Found")