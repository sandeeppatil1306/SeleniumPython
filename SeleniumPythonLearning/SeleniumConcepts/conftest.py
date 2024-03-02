import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I am executing last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Sandeep", "Patil", "sandeepvpatil1984@gmail.com"]


@pytest.fixture(params=[("chrome", "Sandeep"), ("firefox", "Rahul"), ("IE", "Sachin")])
def crossBrowser(request):
    return request.param
