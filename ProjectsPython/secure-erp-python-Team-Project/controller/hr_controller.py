from model import data_manager as manager
from model.hr import hr
from view import terminal as view
from model import util
from datetime import datetime, timedelta, date
from colorama import Fore, Style
from view.terminal import clear_terminal


def list_employees():
    hr_transactions = hr.read_table_from_file(hr.DATAFILE)
    view.print_table(hr_transactions, hr.HEADERS)


def add_employee():
    new_employee = manager.read_table_from_file(hr.DATAFILE)
    data = view.get_inputs(hr.HEADERS[1:])
    data.insert(0, util.generate_id())
    new_employee.append(data)
    manager.write_table_to_file(hr.DATAFILE, new_employee)
    view.print_table(new_employee, hr.HEADERS)


def update_employee():
    list_employees()
    new_employee = manager.read_table_from_file(hr.DATAFILE)
    id = view.get_input("ID of the employee you want to update: ")
    print()
    for employee in new_employee:
        if id == employee[0]:
            updated_name = view.get_input("\nNew Name: ")
            updated_birth_date = view.get_input("\nNew Birth Date: ")
            updated_department = view.get_input("\nNew Department: ")
            updated_clearance = view.get_input("\nNew Clearance: ")
            employee[1] = updated_name
            employee[2] = updated_birth_date
            employee[3] = updated_department
            employee[4] = updated_clearance
            print(employee)

    manager.write_table_to_file(hr.DATAFILE, new_employee)
    view.print_table(new_employee, hr.HEADERS)
  

def delete_employee():
    list_employees()
    employees = manager.read_table_from_file(hr.DATAFILE)
    id = view.get_input("ID of the employee you want to remove: ")

    for employee in employees:
        if employee[0] == id:
            employees.remove(employee)
            break
    manager.write_table_to_file(hr.DATAFILE, employees)
    view.print_table(employees, hr.HEADERS)


def get_oldest_and_youngest():
    list_employees()
    employees = manager.read_table_from_file(hr.DATAFILE)
    birthdays = []
    birthday_dates = []
    for employee in employees:
        birthdays.append(employee[2])
    for date in birthdays:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_date = date_object.date()
        birthday_dates.append(date_date)
    birthday_dates.sort()

    oldest = birthday_dates[0]
    youngest = birthday_dates[-1]

    for i in range(len(employees)):
        if employees[i][2] == str(oldest):
            print(f"{employees[i][1]} is the oldest employee.")
        if employees[i][2] == str(youngest):
            print(f"{employees[i][1]} is the youngest employee.")
    

def get_average_age():
    list_employees()
    employees = manager.read_table_from_file(hr.DATAFILE)
    birthdays = []
    birthdays_separated = []
    for employee in employees:
        birthdays.append(employee[2])

    for birthday in birthdays:
        birthday = birthday.split("-")
        birthdays_separated.append(birthday)

    sum_age = 0
    for i in range(len(birthdays_separated)):
        year = int(birthdays_separated[i][0])
        month = int(birthdays_separated[i][1])
        day = int(birthdays_separated[i][2])
        age = calculate_age(datetime(year, month, day))
        sum_age += age
    age_average = sum_age / len(birthdays_separated)
    age_average = int(age_average)
    print(f"The average age between all employees is {age_average} years.")


def calculate_age(birthdate):
    list_employees()
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def next_birthdays():
    list_employees()
    month_and_days = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
                      '11': 30, '12': 31}
    birthday_check = view.get_input('Enter month and day in "mm-dd" format: ')

    month = int(birthday_check.split('-')[0])
    day = int(birthday_check.split('-')[1])

    input_sum_days = sum(month_and_days[str(i)] for i in range(1, month))
    input_sum_days += day

    employees = manager.read_table_from_file(hr.DATAFILE)
    for employee in employees:
        employee_month = int(employee[2].split('-')[1])
        employee_day = int(employee[2].split('-')[2])

        employee_sum_day = sum(month_and_days[str(i)] for i in range(1, employee_month))
        employee_sum_day += employee_day

        minus_two_weeks = input_sum_days - 14
        plus_two_weeks = input_sum_days + 14
        person_name = employee[1]

        if employee_sum_day in range(minus_two_weeks, plus_two_weeks+1):
            print(f"In the coming two weeks {person_name} will have birthday.")
            print("\n")
            break
            
    if employee_sum_day not in range(minus_two_weeks, plus_two_weeks+1):
        print("No employees will have birthday in the coming two weeks.")
    print("\n")


def count_employees_with_clearance():
    list_employees()
    employees = manager.read_table_from_file(hr.DATAFILE)
    clearance_level = input("Enter the clearance level: ")
    employees_with_clearance = 0
    for employee in employees:
        if int(employee[4]) <= int(clearance_level):
            employees_with_clearance += 1
    print(f"The number ofemployees with this clearance level are {employees_with_clearance}.")


def count_employees_per_department():
    list_employees()
    employees = manager.read_table_from_file(hr.DATAFILE)
    employees_by_department = {}
    for employee in employees:
        if not employee[3] in employees_by_department:
            employees_by_department[employee[3]] = 1
        else:
            employees_by_department[employee[3]] += 1
    print(f"The employees by department are {employees_by_department}.")
 

def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu(f"{Fore.GREEN}\nHuman resources\n{Style.RESET_ALL}", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("\nSelect an operation ")
            print()
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
    else:
        clear_terminal()