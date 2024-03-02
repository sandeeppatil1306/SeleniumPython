import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


'''@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")'''


def test_CrossBrowser(crossBrowser):
    print(crossBrowser[1])
