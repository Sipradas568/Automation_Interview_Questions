class Student():
    
    def display_info(self):
        self.name = input("enter name")
        self.age = int(input("enter the age"))
        

studslist=[]


for i in range(3):
    s1 = Student()
    s1.display_info()
    studslist.append(s1)




for s in studslist:
    print(s)




    


    
