"""
dictionary methods- assignment
 1. create an empty dictionary
 2. ask user to enter name, email, mobile, city, and pin from keyboard
 3. insert above pairs into dictionary.
 4. print all pairs of dictionary using for loop
 5. ask user to enter a different name and replace existing name with new name
 in the dictionary
 6. ask user to enter a key and if that key is available in the dictionary remove
 that pair
 7. ask user to enter a value and check if that value exists in the dictionary
 8. ask user to enter state, and insert that pair into dictionary.

"""
empty_dic={}
name=input("Enter Your Name : ")
email=input("Enter Your Email Please : ")
mobile=input("Enter Your Mobile Number : ")
city=input("ENter Your City Name : ")
pin=input("Enter Your City Pin Code : ")

empty_dic['name']=name
empty_dic['email']=email
empty_dic['mobile']=mobile
empty_dic['city']=city
empty_dic['pin']=pin

for k,v in empty_dic.items():
    print(f'{k} ":"{v}' )

new_name=input('Enter New Name : ')
empty_dic['name']=new_name

print("Updaed Dictionary With New Name ",empty_dic)

use_key=input("Enter A Key To Delete :")

if use_key in empty_dic:
    empty_dic.pop(use_key)
    print(f'{use_key} Delete Successfully')
else:
    print("Invalid key")

print("Updaed Dictionary Delete ",empty_dic)

userValue=input("Enter A Value To Check The Value Is Exit Or Not : ")
if userValue in empty_dic.values():
    print(f'{userValue} Is Exit In This Dictionary')
else:
    print("Value IS Not Exit")


user_state=input("Enter Your State Name : ")
empty_dic['state']=user_state

print(f"finally dictionary {empty_dic}")