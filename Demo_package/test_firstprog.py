

import pytest

@pytest.mark.usefixtures("setup")

class Testexample:
    def testGoodMorning(self):
        print("Hi Good Morning!")

    def testsecmethod(self):
        a = 2
        b=1
        assert a+b == 3, "Output is not correct"
        



    