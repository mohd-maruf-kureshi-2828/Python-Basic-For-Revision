"""
with open('practice.txt','w') as f:
    f.write('hey my name is Mohamed Maruf Kureshi \n')
    f.write('Now I am Learning File Handling In Java \n')
    f.write('I am a java full stack developer')
"""

"""
with open('practice.txt','r') as f:
    data=f.read()
    newData=data.replace('java','python')

with open('practice.txt','w') as f:
    f.write(newData)
"""

"""
with open('practice.txt','r') as f:
    world=input('Enter A World To Check IS Have In File Or Not :')
    if world in f.read():
        print(f'Yes {world} Is This World Have On This File ')
    else:
        print(f'{world} Sorry This World Not In This File')

"""

"""
world=input('Enter a character or world to find its line number :')
data=True
line_no=1
with open('practice.py','r') as f:
    while data:
         data = f.readline()
         if world in data  :
            print(f'{world} Yes Is Present {line_no}')
         line_no+= 1
"""


# ab hum ak file bana ge aur usme number dare ge fir check kare ge even koun se hai 
"""
with open('practice_even.txt','w') as f:
    f.write('1,2,3,4,5,6,7,8,10,11,12,13,14,15')
"""

count=0
with open('practice_even.txt','r') as f:
    data=f.read()
    nums=data.split(',')
    for i in nums:
        if (int(i) % 2 == 0):
            count += 1
print(count)

