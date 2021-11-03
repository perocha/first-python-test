'''
Read a file
   "r" --> Read
   "w" --> Write
   "a" --> Append info without changing the main file
   "r+" --> Read and Write
'''
employee_file = open("employees.txt", "r+", encoding="utf-8")

print (employee_file)

for employee in employee_file.readlines():
    print (employee)

employee_file.write ("\nJuana, Tester")

employee_file.close()
