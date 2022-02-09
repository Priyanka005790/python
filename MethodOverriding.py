#base class
class User:
    def getinfo(self):
        print("learn python")
class Employee(User):
    def getinfo(self):
        print("welcome to python")
e1 = Employee()
e1.getinfo()