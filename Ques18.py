inp = "Get the latest news updates and breaking news stories from India and around the world right here. 2008"

lst = inp.split()
str= ""
str1 = ""
for i in lst:
    if i[0]== 'a' or i[0]== 'A':
        str = str+i+" "
print(str)

for i in lst:
    if i[0] in ('0','1','3','4','5','6','7','8','9','2'):
        str1 = str1 + i + " "
print(str1)


