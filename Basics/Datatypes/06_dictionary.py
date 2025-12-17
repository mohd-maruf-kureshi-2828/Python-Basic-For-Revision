my_dic={
    'name':'maruf',
    'age':24,
    'course':'BCA'
}
my_dic['skills']='Python Full Stack'
# print(my_dic,type(my_dic))


# assignment
details={
    'eno':1,
    'ename':'Arbaz',
    'esal':2500
}

details.update({'esal':5000})
details['place']='Bangalore'
# print(details)


# for dic in details:
#     print(dic,details[dic])

# for item in details.items():
#     print(item)


"""
assignment
 1.read from keyboard: house number, street, city , pincode
 2.store into a dictionary
 3.print dictionarypairs one by one using for loop
"""

# house_number=int(input('Enter Your House Number 🏠: '))
# street=input('Enter Your Street : ')
# city=input('Enter Your City 🏢 : ')

# userDetails={
#     'House Number':house_number,
#     'street':street,
#     'city':city,
# }
# print("\nYour Address Details👇")
# for k,v in userDetails.items():
#     print(k,":",v)