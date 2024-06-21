# input = Hi I am Sipra Das
#output= H m Spr Ds
inp = input("enter a string")
str= ""
for i in inp:
    if i not in ('a','e','i','o','u'):
        str=  str+i
        
print(str) 