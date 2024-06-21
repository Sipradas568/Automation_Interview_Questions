
import pytest

@pytest.mark.usefixtures("credentials")

class TestExample2:
     


     def testsecprog(self):
        print("Hello")



     def testlogin(self,credentials):
         un, pwd = credentials
         print(un)
         print(pwd)

     
         
         
         
         




   