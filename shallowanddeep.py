 <-------In this new reference Variable will be created---->
#this is called aliasing
l1=[10,20,40,50]
l2=l1
l2[2]=90
print(l1)
#[10, 20, 90, 50]
print(l2)
#[10, 20, 90, 50]


'''
<-------In this new object will be created  (cloning)---->
l1=[10,20,40,50]
l2=l1.copy()
l2[2]=90
print(l1)
[10, 20, 40, 50]
print(l2)
[10, 20, 90, 50]


<----------->
Shallow copy:
and Shallow cloning
<-----If the original contains any refrences to mutable object,
just duplicate reference variable will be created pointing to old 
contained objects,but not duplicate objects creations 
----->

import copy
l1=[10,20,[100,440],90]
l2=copy.copy(l1)
l2[2][0]=888
print(l1)
[10, 20, [888, 440], 90]

print(l2)
[10, 20, [888, 440], 90]

print(id(l1[2]))
2412269998536
print(id(l2[2]))
2412269998536
<------>
deep copy:
Complete duplicate objects
It is costly operation
import copy
l1=[10,20,120,90]
l2=copy.deepcopy(l1)
l2[2]=888
print(id(l1[2]))
140705658692352
1898647026064
print(id(l2[2]))
1898647026064
print(l1)
[10, 20, 120, 90]
print(l2)
[10, 20, 888, 90]


<-------String  also called-------->
 This is also called shallow copy
l1=[10,20,40]
l2=l1.copy()
print(l1)
[10, 20, 40]
print(l2)
[10, 20, 40]

'''







