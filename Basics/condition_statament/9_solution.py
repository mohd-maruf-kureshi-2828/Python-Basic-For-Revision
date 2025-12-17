year=int(input("Enter A Year To Cheak Leap Year Or Not :"))

if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0):
    print(f"{year} Its A Leap Year")
else:
    print(f"{year} not a leap year")