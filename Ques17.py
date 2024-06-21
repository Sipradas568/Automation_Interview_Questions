Input = "Get the latest news updates and breaking news stories from India and around the world right here. 2008"

lst = Input.split()

str1= " ".join(lst[0:5])
print(str1)
for i in lst:
    if i == "2008":
        print(i)