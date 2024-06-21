import pytest

@pytest.fixture(params= [("sipea",96),"sipra","prabhat","990234"])

def pr(request):
    return request.param