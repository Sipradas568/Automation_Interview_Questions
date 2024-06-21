inp = "I am Sipra Prabhatmahar Das"
#op = longest substring
lst = inp.split()
longest = inp[0]
for i in lst:
   
    if len(i)>len(longest):
        longest = i
print(longest)
    
