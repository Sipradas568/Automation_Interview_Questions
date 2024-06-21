def evenodd(str):
    
    for i in str:
        ctr=0
        for j in str:
            if i==j:
                ctr=ctr+1
        if ctr%2 ==0:
            print("{} is of even occu" .format(i))
        else:
            print("{} is of odd occu" .format(i))
str2= input("enter a string ")
evenodd(str2)


        