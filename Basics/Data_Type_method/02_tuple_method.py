"""
tuple methods- assignment
 1. take an empty tuple
 2. insert 5 elements from keyboard
 3. ask user to enter an element from keyboard,and  delete that element from
 tuple
 4. ask user to enter an element from keyboard and print the position of that
 element
"""

empty_tup=()
print("Enter 5 Element 👇 ")
for i in range(5):
    elemet=int(input("Enter Element :"))
    empty_tup=empty_tup+(elemet,)
print("\nTuple elements are:",empty_tup)


del_user=int(input("Enter A Element U Want To Delete : "))

if del_user in empty_tup:
    tempary_list=list(empty_tup)
    tempary_list.remove(del_user)
    empty_tup=tuple(tempary_list)
    print("Element Delete Sucessfully 🎉")
else:
    print("Invalid Element")

print(f'\nUpdated Tuple🎉 : {empty_tup}')

search_pos=int(input("Enter A Elemnt To Find Its Position🎉:"))
if search_pos in empty_tup:
    position=empty_tup.index(search_pos)
    print(f"The Element Found At Position 🎉 {position}")
else:
    print("No Element On This Position")