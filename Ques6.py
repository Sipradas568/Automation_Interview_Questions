inp = "Sipra Das mindfire"
lis = inp.split()
lt= []
for i in lis[:-1]:
    str = i.replace(i[1:],".")
    
    lt.append(str)
    st =" ".join(lt)


for i in lis[-1:]:
    str4 = i.capitalize()


print(st+str4)