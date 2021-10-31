monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print (type(monthConversions))
print (monthConversions)

print (monthConversions["Jan"])
print (monthConversions.get("Dec"))
print (monthConversions.get("Test"))
print (monthConversions.get("Test", "Not a valid key"))
