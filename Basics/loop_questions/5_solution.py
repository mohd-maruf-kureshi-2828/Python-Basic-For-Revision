repeated_char=input("Check Unique Character : ")

for char in repeated_char:
    if repeated_char.count(char)==1:
        print("unique char is :",char)
        break