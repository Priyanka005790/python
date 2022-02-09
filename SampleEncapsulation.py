#private public pretectes
class car:
    def __init__(self, name, course):
        self._name = name                   #prectected variable
        self.course = course                #public variable
    def description(self):
        return f"{self._name} is learning {self.course}"
obj = car("John", "Python")
#accessing pretected variable via class method
print(obj.description())
#accessing protected variable directly from outside
print(obj._name)
print(obj.course)

