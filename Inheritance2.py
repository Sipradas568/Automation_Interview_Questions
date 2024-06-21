class Parent:
    num = 10
    
    def method1(self, a, b):
        self.a = a
        self.b = b
        c = self.a + self.b
        print(c)

class Child:
    print(Parent.num)  # Accessing the num variable from the Parent class

# Creating an instance of Child class
child_obj = Child()
# Calling method1 of Parent class using Child class instance
child_obj.method1(3, 5)
