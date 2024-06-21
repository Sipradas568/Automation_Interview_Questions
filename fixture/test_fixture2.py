import pytest

@pytest.mark.usefixtures("pr")

def testfunc(pr):
    print(pr[1])