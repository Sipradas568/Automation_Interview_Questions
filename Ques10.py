input = "PythonProgramming"
str = input.lower()
for i in str:
    ctr=0
    for j in str:
        if i ==j:
            ctr=ctr+1
    print("{} {}" .format(i,ctr))
