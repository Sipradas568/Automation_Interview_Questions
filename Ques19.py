inp = [8,9,10,95,1,2,0]
large = inp[0]
small = inp[0]
for i in range(0,len(inp),1):
    for j in range(0,len(inp),1):
        if inp[i]>large:
            large = inp[i]
        elif inp[i]<small:
            small = inp[i]
            
print("largest is {}" .format(large))
print("smallest is {}" .format(small))


