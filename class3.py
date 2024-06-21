class class3:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        ch = int(input("enter the choice"))
        if ch ==1:
            print("performing addition: " + str(a+b))
        elif ch ==2:
            print("performing substraction: " + str(a-b))
            
        elif ch ==3:
            print("performing multiplication: " + str(a*b)) 
        else:
            print("out of choice")

class3(5,6 )
class3( 100,20)
            
            


