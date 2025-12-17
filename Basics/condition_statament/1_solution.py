Age=int(input("Enter Your Age : "))

if Age < 13:
    print(f"Your Age Is {Age} , Child")
elif Age >= 13 and Age <= 19:
     print(f"Your Age Is {Age} , Teenager")
elif Age > 19 and Age <= 59:
     print(f"Your Age Is {Age} , Adult")
else:
     print(f"Your Age Is {Age} , senior")
    