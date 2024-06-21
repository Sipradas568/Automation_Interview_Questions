inp = "cuttack is in Odisha and Bhubaneswar is also y in odisha"

lst = inp.split()
for i in range(len(inp)):
    for j in range(0,len(lst)-1,1):
          if len(lst[j])>len(lst[j+1]):
              lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)

        

  


        

    


    
    
    
