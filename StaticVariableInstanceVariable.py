#class for computer science Student
# class CSStudent:
#     stream = 'cse'      #class variable or static variable
#     def __init__(self,name,roll):
#         self.name = name        #instance variable
#         self.roll = roll        #instance variable
#
# #objects of CSStudent class
# a = CSStudent('John',1)
# b = CSStudent('Tom',2)
#
# print(a.stream) #print cse
# print(b.stream) #print cse
# print(a.name) #print john
# print(b.name) #print tom
# print(a.roll) #print 1
# print(b.roll) #print 2
#
# #class variable can be accessed using class
# #name also
# print(CSStudent.stream)     #print cse
#
# #if are change the stream for first a if cant be changed from b
# a.stream = 'ece'
# print(a.stream)     #print ece
# print(b.stream)     #print cse

#to change the stream for all instance of the class as can change it
#directly from the class
# CSStudent.stream = 'mech'
#
# print(a.stream) #print ece
# print(b.stream) #print mech

class example:
    staticVariable = 9   #Access through class
print(example.staticVariable) #given 9

#Access through an instance
instance = example()
print(instance.staticVariable) #again give 9

#change within an instance
instance.staticVariable = 12
print(instance.staticVariable)  #gives 12
print(example.staticVariable) #give 9







