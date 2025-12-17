Age=int(input("Enter Your Age : "))
day=input("Enter Day : ")

# if Age <= 12 and day == 'Wednesday':
#     print(f"Your Age Is {Age} Price Is $8 and You Got $2 Discount Because Today Is {day}")
# elif Age >= 12 and day == 'Wednesday':
#     print(f"Your Age Is {Age} Price Is $12 and You Got $2 Discount Because Today Is {day}")
# elif Age <= 12:
#      print(f"Your Age Is {Age} Price Is $8 and You Dont Got $2 Discount Because Today Is  {day}")
# else:
#      print(f"Your Age Is {Age} Price Is $12 and You Dont Got $2 Discount Because Today Is {day}")    


# new syntax
price=12 if Age >= 18 else 8

if day.lower() == "wednesday":
    price = price-2
print(price)