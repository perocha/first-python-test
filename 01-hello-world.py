print ("hello world updated!")

name = "Pedro"
age = "47"
print (f"My name is {name} and my age is {age}")
print ("My name is " + name + " and my age is " + age)


print (name.capitalize())
print (name.casefold())
print (name.isalpha())
print (name.isalnum())
print (name.upper())
print (name.lower())

index = 0
while index < len(name):
    print (name[index])
    index += 1

print (name.index("e"))
name = "Pedroooo"
print (name.index("o"))

print (name.replace ("o","a"))