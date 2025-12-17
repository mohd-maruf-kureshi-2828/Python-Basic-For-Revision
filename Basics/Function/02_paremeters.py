"""
 typesof parameters:
1.positionalparameters 
2.keyword parameters 
3.default parameters
c(or) variable no. of parameters
5.keyword arbitrary parameters variableno. of keyword parameters
"""

# 1.positionalparameters 
# def pos(num1,num2):

# 2.keyword parameters 
# def keypar(num1,num2):
#     print(f' num 1 is {num1}')
#     print(f'num 2 is {num2}')
# keypar(num2=20,num1=10)

# 3.default parameters
# def details(name="maruf",course="BCA"):
#     print(f'name is {name}')
#     print(f'course is {course}')
# details('umair','B.Com')

# 3.default parameters
# def arb(*names):
#     print(f'names is {names}')
# arb('maruf','umail','arbaz','arshad')

# def arb2(age,*name,course):
#     print(f'age is {age} belong to this people {name} and course is {course}')
# arb2(20,'maruf','umair','arbaz','vivek',course="BCA")

#with for loop
# def arb2(*a):
#     for i in a:
#         print(i , end=',')
# arb2("maruf","arbaz","vivek","sufiyan") 


# 5 keyword arbitrary parameters
# def funtion(**kwars):
#     for k,v in kwars.items():
#         print(k,':',v) 
# funtion(name="maruf",age=24,profesion='Full Stack Developer')


"""
assignment
 1.your writing a project in python for a hospital.write a method which takes patient values.
 below are conditions for passing patient values.
 a)every patient gives name
 b)every patient gives blood group
 c)every patient gives what all the diseases suffering. remember that
 apatient may be suffering from multiple diseases.
 d)some patient gives email ids , some will not give.
"""

"""
solution

def patientDetails(name,blood,*diseases,email='default thank You'):
    print(f'patient name Is {name}👨 , patient blood group is {blood}🩸, patient Disease is {diseases}😷 and email  is {email}')

patientDetails("arbaz", 'b', 'Mental Issues,Overthing,depression,overconfident', email='@arbaz.com')

"""
"""
2.your are writing a python application for a training institute. write a method.
 which takes student values. below are the conditions for passing student values.
 a)every student has name
 b)some student may give 1 email id, or 2 or more.
 c)students will also give their house address in different formats.

"""
"""
solution 

def trainingInstitute(name,*gmail,**kwarbt):
    print(f'Student name {name} student gmail is {gmail} student address is {kwarbt}')

trainingInstitute('john','@john.com','@personalJohn.com',pincode=5212212,street='behind GFGC College',Religion='Asia')

"""