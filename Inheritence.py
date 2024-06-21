class Parent:
    num = 10
    def method1(self,a,b):
        self.a = a
        self.b = b
        self.c= a + b
        print(self.c)

class child(Parent):
    print(Parent.num)
    print(Parent.a)
    
    
    

obj = child()
print(obj.method1(2,3))


