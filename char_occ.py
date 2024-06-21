str = input("enter a string ")
str2 = str.lower()
for i in str2:
    ctr =0
    for j in str2:
        if i ==j:
            ctr = ctr + 1
    print(f"occurrence of {i} is {ctr}")
   

    







  