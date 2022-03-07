print("Welcome to the Employee Record Management!")
Number_of_employees = int(input("Please enter the number of employees: "))


for index in range(Number_of_employees):
    Employee_first_name = input("Please state your first name: ")
    while len(Employee_first_name) == 0:
        print("Invalid data, please enter again: ")
    Employee_last_name = input("Please state your last name: ")
    while len(Employee_last_name) == 0:
        print("Invalid data, please enter again: ")
    Employee_age = int(input("Please state your age: "))
    age = int(Employee_age)
    while (age < 18) or (age > 100):
        print("Invalid data, please enter again")

    print(f"Employees name is {Employee_first_name} {Employee_last_name} and their age is {Employee_age}.")
Age_sum = 0
Age_sum = Age_sum + age
if Age_sum > 500:
    print("Warning! Age Sum is over 500")