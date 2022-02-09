class Calculate:
    def add(self,a,b):
        print("a+b={}".format(a+b))
    def add(self,a,b,c):
        print("a+b+c={}".format(a+b+c))
c1 = Calculate()
c1.add(10, 20, 30)
# c1.add(10,20)

#using variable length arguments

class Calculate:
    def add(self, *args):    #variable length arguments
        result = 0
        for param in args:
            result += param
        print("Result:{}".format(result))

c1 = Calculate()
c1.add(10,20,30)
c1.add(10,20)
