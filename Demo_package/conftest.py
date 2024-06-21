import pytest

@pytest.fixture(scope="class")



def setup():
    print("set it up")
    yield
    print("close it")
        



def credentials():
    return("sipra","sipra123")
    
