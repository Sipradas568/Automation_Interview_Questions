inp = "I am a good girl but i am not not a selfish not girl" #occurence of substrings

lst1 = inp.split()
for i in lst1:
    ctr=0
    for j in lst1:
        if i.lower()==j.lower():
            ctr=ctr+1
    print("{} ocurrence is {}"  .format(i,ctr))

