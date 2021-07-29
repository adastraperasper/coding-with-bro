employees_file = open("employees.txt", "r+")

for employee in employees_file.readlines():
    print(employee)
print(employees_file.readlines())



employees_file.close()
