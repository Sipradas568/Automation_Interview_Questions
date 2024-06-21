#inp = Sipra Deas
#out= iaea SprDs

str = "Adas Supr"
str2 = ""
str3= ""
str1 = str.lower()
for i in str1:
    if i in ('a','i','e','o','u'):
        str2 = str2+i
    else:
        str3 = str3+i
        str4 = str3.replace(" ", "")
print(str2+ " "+str4)




