# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# total_positive = [num for num in numbers if num >= 0]
# print(total_positive)

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number=0

for i in numbers:
    if i>=0:
        positive_number += 1
print("total positive number in list is : ",positive_number)