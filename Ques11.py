input= "I am Sipra Das"
#o/p= "I ma arpis saD"
#o/p = "ma I saD arpis"

lst1 = []
lst2= []
lst = input.split()
for i in lst:
    str1 = i[::-1]
    lst1.append(str1)

for i in range(0,len(lst1)-1,1):
    if i %2 == 0:
        lst2.append(lst1[i+1]+" "+lst1[i])
print(" ".join(lst2))

    
   
    



