# class Student:
#     def __init__(self,name,marks,age):
#         self.name=name
#         self.marks=marks
#         self.age=age
#         print(name,marks,age)
#         print('adding new student in Database...')

# s1=Student('arbaz',89,20)
# s2=Student('Umair',90,20)


#two types of attribute class attribute object attribute
class Student:
    # default constructor
    # class attribute 
    college_name='GFGC'
    def __init__(self):
        pass

    # parameter constructor
    def __init__(self,name,age):
    #    object attribute
        self.name=name
        self.age=age

    def hello(self):
        print(f'hello just for fun',self.name)

# s3=Student('ali',20)
# s3.hello()