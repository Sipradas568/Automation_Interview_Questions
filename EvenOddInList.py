input = [1,2,1,2,3,4,5,6,7,7,7,8,8,9,9]

for i in input:
    ctr=0
    for j in input:
        if i==j:
            ctr = ctr+1
    if ctr%2 ==0:
        print("{} has even occurence" .format(i))
    else:
        print("{} has odd occurence" .format(i))
