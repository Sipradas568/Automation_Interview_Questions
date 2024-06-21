inp = "I am sipra Das"
#op= Iaiaa maprDs
str2 = ""
str3 = ""
for i in inp.lower():
    if i in ('a','e','i','o','u'):
        str2 = str2+i
    else:
        str3 = (str3+ i).strip()
print(str2+" " +str3)


