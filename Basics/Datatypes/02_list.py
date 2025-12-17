# my_list=["maruf",24,"BCA"]
# print(my_list,type(my_list))
# my_list[1]=11
# print(my_list)


# list assignment
# x=[100,200,300,400]
# print(x[-1])  #output 400
# print(x[1])  #output 200
# print(x[0:]) #output  [100,200,300,400]
# print[x[:10]] #error out of range
# x[0]=x[-1]
# print(x)



#list assignment 2
# x=[100,200,300,400,500]
# print(x[0:3]) #output [100,200,300]
# print(x[1]+x[2]) #output [500]
# x[3]=x[4]
# print(x)



#for loop in list
my_list=[10,20,30,40,50,60]
# for i in range(0,5):
#     print(my_list[i])

# for i in range(len(my_list)):
#     print(my_list[i])

# for i in my_list:
#     print(i)


# for i in range(5,-1,-1):
#     print(my_list[i])


#assignment step 2, 10,30,50
# nums=[10, 20, 30, 40, 50, 60, 70, 80,90,100]
# for i in range(0,len(nums),2):
    # print(nums[i])
    # print(i) indexing printing


# List withloop assignment  :
#  Calculate the sum of elements present in list using for loop.
# my_list = [10, 20, 30, 40, 50]
# total=0
# # for i in range(len(my_list)):
#     total=total+my_list[i]
# print(total)

# second method
# for i in my_list:
#     total=total+i
# print(f'total number is {total}')


# List withloop assignment4:
#  Find the biggest element present in list
my_list = [10, 200, 30, 400, 50]
biggest=0
for i in my_list:
    if i > biggest:
        biggest = i
print(biggest)