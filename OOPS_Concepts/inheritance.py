class Samsung:
    def __init__(self):
        print("I am Samsung")

    def makeScreens(self):
        print("Samsung makes best screens for phones")

    def screenTest(self):
        print("Screen Test1: OK")
        print("Screen Test2: OK")
        print("Screen Test3: OK")


class Apple(Samsung):
    def __init__(self):
        print("I am Apple")


    def a15Chip(self):
        print("Iphone 13 has a15 bionic chipset")

    def itest(self):
        print("Apple chipset test: Pass")
        super().screenTest()

    #methodoverriding
    def makeScreens(self):
        print("Apple also makes screens for phones")

user = Apple()
user.a15Chip()
user.makeScreens()
user.itest()
user.makeScreens()