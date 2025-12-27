"""
write mode file agar file nhi hoge tu bhi automatic ban jaye ge
f=open('demo.txt', 'w')
data=f.write('Hello, World!')
f.close()

"""

"""
f=open('demo.txt','r')
# data=f.read()
data=f.readline()
print(data)
f.close
"""

"""
f=open('demo.txt','a')
f.write('\nI am a python full stack developer')
f.close()

"""

"""
with open('demo.txt','r') as f:
    data=f.read()
    print(data)
"""
import os
os.remove('demo.txt')