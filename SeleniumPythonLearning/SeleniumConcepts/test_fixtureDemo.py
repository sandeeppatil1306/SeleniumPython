import pytest

'''@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute step in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute step in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute step in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute step in fixtureDemo3 method")'''


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
