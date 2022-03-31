employee_file = open("/media/ashwin/Volume/Others/Development/Python/Tutorial/26-reading-a-file/employees.txt", "r")

print(employee_file.readable())
# print(employee_file.read()) -> read the file
# print(employee_file.readline()) -> read line 1
# print(employee_file.readline()) -> read line 2
# print(employee_file.readlines()) -> prints array of elements
# print(employee_file.readlines[0]) -> read first element of array

for employee in employee_file.readlines():
    print(employee)

employee_file.close()