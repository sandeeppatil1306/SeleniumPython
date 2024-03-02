class Calculator:
    num = 100

    def getData(self):

        print("I am now executing as a method in class")

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am a constructor , and called automatically when object is created")

    def summation(self):
        return self.a + self.b





obj = Calculator(2, 3)
obj.getData()
print(obj.num)
print(obj.summation())

# obj = Calculator()
# obj.getData()
# print(obj.num)
