#List
list=['abcd',786,2.23,'john',70.2]
tinylist=[123,'john']

print(list)             #prints completd list
print(list[0])          #print first element of the list
print(list[1:3])        #prints elements starting from 2nd till 3rd
print(list[2:])         #prints elements starting from 3rd element
print(tinylist * 2)     #prints list two time
# print(list * tinylist)  #prints concatenated list

#iterate over the list using index
# a = ['priyanka','pawar','python']
# for i in range(len(a)):
#     print(a[i],end=" ")

# #1.insert                             #it is used to insert an item at a given position
# #List
# list1 = [1,2,3,4,5,6]
# #Inserting values
# list1.insert(0,7)       #adding a no 7 at position 0:
# print("new list",list1)


# #2.append
# a=[1,2,3,4]
# print(a)                            #add an element to the end of the list.a[len(a):]=[x] Add the new no to list
# a.append(5)
# print("updated list:",a)


# #3.remove()
# list1=[3,4,1,1,8,9]             #remove the first item from the list
# list1.remove(4)
# print(list1)


# #Pop()
# a=["python","java","c++","php"]                 #remove an element specified position using index value in the pop
# #remove java
# print(a.pop(1))
# print(a)

#Reverse()              #reverse the element of the list in place.it will modify the orgininal list
# list1 = [1,4,3,6,7]
# #reversing list
# list1.reverse()
# print(list1)