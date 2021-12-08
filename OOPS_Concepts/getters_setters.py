class Student:
    def setName(self,n):
        self.__name = n

    def getName(self):
        return self.__name

    def setMarks(self,m):
        self.__marks = m

    def getMarks(self):
        return self.__marks

    def display(self):
        print("Name :", self.__name) #we can also write self.getName() and self.getMarks()
        print("Marks :",self.__marks)

S = Student()
S.setName('John')
S.setMarks(90)
S.display()