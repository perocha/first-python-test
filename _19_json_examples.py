'''
Example of using json
'''
import json
import requests

#
# Open a file and deserialize as json
#
with open("file-example.json", "r", encoding="utf-8") as my_file:
    file_data = my_file.read ()

my_json_info = json.loads (file_data)

print (my_json_info)

#
# Example to get a json from http request
#
http_response = requests.get ("https://jsonplaceholder.typicode.com/todos")
todo_list = json.loads (http_response.text)

print (type(todo_list))
print (todo_list[:5])              # prints 5 first items from the json

# Count all completed TODOs for each user
todos_completed_by_user = {}
for todo in todo_list:
    if todo["completed"]:
        try:
            # New completed TODO for this user
            todos_completed_by_user[todo["userId"]] += 1
        except KeyError:
            # User not counted yet, first count
            todos_completed_by_user[todo["userId"]] = 1
print (todos_completed_by_user)

# Filter only TODOs from userId = 1
my_list = [x for x in todo_list if x["userId"] == 1]
print (f"Total list size = {len(todo_list)}")
print (f"Filtered list size with TODOs from user 1 = {len(my_list)}")

# Filter only completed TODOs
my_list = [x for x in todo_list if x["completed"]]
print (f"Filtered list size with completed TODOs = {len(my_list)}")

# Filter only pending TODOs (not completed) for user 1
my_list = [x for x in todo_list if not(x["completed"]) and x["userId"] == 1]
print (f"Filtered list size with completed TODOs from user 1 = {len(my_list)}")
print (my_list)

# Write the filtered json into a new file
with open("filtered-file-example.json", "w", encoding="utf-8") as data_file:
    json.dump(my_list, data_file, indent=2)
