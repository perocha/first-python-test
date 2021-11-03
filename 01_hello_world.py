print ("hello world updated!")

MyName = "Pedro"
MyAge = "47"
print (f"My name is {MyName} and my age is {MyAge}")
print ("My name is " + MyName + " and my age is " + MyAge)


print (MyName.capitalize())
print (MyName.casefold())
print (MyName.isalpha())
print (MyName.isalnum())
print (MyName.upper())
print (MyName.lower())

Index = 0
while Index < len(MyName):
    print (MyName[Index])
    Index += 1

print (MyName.index("e"))
name = "Pedroooo"
print (MyName.index("o"))

print (MyName.replace ("o","a"))