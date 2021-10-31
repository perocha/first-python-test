mytuple = ("apple", "cherry", "banana")     # parentesis
mylist = ["apple", "cherry", "banana"]      # brackets

print ("\n ** Print list and tuple")
print (mytuple[0])
print (mytuple[1])
print (mytuple[2])
print (mylist[0])
print (mylist[1])
print (mylist[2])

# mytuple[1] = "strawberry" ----> this will return an error, tupple are unchangeable
mylist[1] = "strawberry"

print ("\n ** We can change the list, but cannot change the tuple")
print (mytuple)
print (mylist)

print ("\n ** Check the var type of tuple and list")
print (type(mytuple))
print (type(mylist))

print ("\n ** Tuple with several items")
coordinates = ((4, 5), (6, 7), (80, 34))
print (type(coordinates))
# coordinates [1] = (5, 9) ----> this will return an error, tupple are unchangeable

coordinates_list = [(4, 5), (6, 7), (80, 34)]
print (type(coordinates_list))
print (coordinates_list)
coordinates_list.append((6, 9))
print (coordinates_list)
coordinates_list [1] = (5, 9)
print (coordinates_list)
