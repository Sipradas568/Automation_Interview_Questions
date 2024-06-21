class const:
    def __init__(self):
        print("i am the constructor")

    def calc(self,a,b):
        self. a = a
        self.b = b
        return(self.a+self.b)
    

obj = const()
print(obj.calc(4,5))
        
        