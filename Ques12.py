inp = "Sipra Das Gram"
#o/p = "S.D.G."

lst1 = inp.split()
lst2 = []
for i in lst1:
    str1 = i.replace(i[1:],'.')
    lst2.append(str1)


print(" ".join(lst2))