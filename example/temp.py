# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
string = "Hello Data Scince"
print (string)

list = [1,3,5,6,12,456]
print (list)
#x = int(input("Input a number:"))
#if x < 0:
 #   x = 0
 #   print("it is X<0")
#elif x >1:
 #   print("it is x>1")
#else:
 #   print("more")
    
for i in list[:]:
    if i >6:
        print (i)
    else:
        print (i-6)
        
def func(n):
    if n>0:
        print(n)
        list.append(n)
        print(list)
    else:
        n+100
        print(n)
        list.append(n)
        print(list)
    print("func is end !")
    
def func2():
    strTemp = ""
    strTemp = str(input("Input a string !:"))
    if len(strTemp) >6:
        print("This string letters is >6")
         # how to join two string into a string 
        print(string+strTemp)
    else:
        print(strTemp)
    print("this's all")
    