Animal="cat"
age=2

if Animal == "dog" and age <= 2:
    print("puppy food")
elif Animal == "cat" and age >= 5:
    print("Senior cat food")
elif Animal == "cat" and age < 5:
    print("child food")
else:
    print("adult food")