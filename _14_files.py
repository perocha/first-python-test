'''
Read a file
   "r" --> Read
   "w" --> Write
   "a" --> Append info without changing the main file
   "r+" --> Read and Write
'''
with open("employees.txt", "r+", encoding="utf-8") as file_handle:
    print (file_handle)

    for employee in file_handle.readlines():
        print (employee)

    file_handle.write ("\nJuana, Tester")
