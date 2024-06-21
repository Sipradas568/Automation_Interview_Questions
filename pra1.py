inp = "This is testing practice"
#op = is practice This testing

lst = inp.split()
for i in range(0,len(lst)-1,1):
    for j in range(0,i-1,1):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]= lst[j+1],lst[j]
print(lst)


#is this testing practice


