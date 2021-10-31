companies = ["Microsoft", "Google", "Apple", "Amazon", "IBM"]

print ("** Print the complete list:")
print (companies)

print ("\n** Print from the 2nd item:")
print (companies[1:])

print ("\n** Print from the 2nd item to the 3rd:")
print (companies[1:3])

print ("\n** Print index 0 and 2:")
print (companies[0])
print (companies[2])

print ("\n** Print index -1 and -3:")
print (companies[-1])
print (companies[-3])

print ("\n** Loop the list with FOR:")
for companyName in companies:
    print (companyName)

print ("\n** Change the 5th item:")
companies[4] = "Tesla"
print (companies)

print ("\n** Append:")
companies.append ("Surprise")
print (companies)
print ("The size of the list is now " + str(len(companies)))

print ("\n** Extend the list with another list:")
number_list = [15, 31, 23, 6, 42, 1]
companies.extend (number_list)
print (companies)

print ("\n** Insert a new item:")
companies.insert (1, "New")
print (companies)

print ("\n** Remove one of the items:")
companies.remove ("New")
print (companies)

print ("\n** Pop (remove) 6 items from the list:")
companies.pop ()
companies.pop ()
companies.pop ()
companies.pop ()
companies.pop ()
companies.pop ()
print (companies)

print ("\n** Return the index of a given list item")
print (companies.index ("Microsoft"))

print ("\n** Count the times a given list item is in the list")
print (companies.count ("Microsoft"))
companies.append ("Microsoft")
print (companies.count ("Microsoft"))

print ("\n** Sort and reverse the list")
companies.sort()
print (companies)
companies.reverse()
print (companies)
number_list.sort()
print (number_list)

print ("\n** Copy and then remove all items from the list:")
companies_list2 = companies.copy()
companies.clear()
print (companies)
print (companies_list2)