weather=input("Today Is Weather Sunny,Rainy,Snowy : ")

if weather.lower() == "sunny":
    print("Go for a walk, Rainy")
elif weather.lower() == "Rainy":
    print(" Read a book ")
elif weather.lower() == "snowmy":
    print(" Build a snowman ")
else:
    print("Enter Weather Only Give")