print("Welcome to the Employee Record Management!")
Number_of_employees = int(input("Please enter the number of employees: "))


for index in range(Number_of_employees):
    Employee_first_name = input("Please state your first name: ")
    while len(Employee_first_name) == 0:
        print("Invalid data, please enter again: ")
    Employee_last_name = input("Please state your last name: ")
    while len(Employee_last_name) == 0:
        print("Invalid data, please enter again: ")
