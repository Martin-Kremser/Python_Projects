from model import data_manager as manager
from view import terminal as view
from model.crm import crm
from model import util
from colorama import Fore, Style
from view.terminal import clear_terminal


def list_customers(): 
    customers = manager.read_table_from_file(crm.DATAFILE)
    view.print_table(customers,  crm.HEADERS)  


def add_customer():  
    new_customer = manager.read_table_from_file(crm.DATAFILE)
    data = view.get_inputs(crm.HEADERS[1:])
    data.insert(0, util.generate_id())
    while data[3].lower() != 'yes' and data[3].lower() != 'no':
        data[3] = view.get_input("Subscribed? yes or no ")
    if data[3] == "yes":
        data[3] = "1"
    elif data[3] == "no":
        data[3] = "0"
    new_customer.append(data) 
    manager.write_table_to_file(crm.DATAFILE, new_customer)
    view.print_table(new_customer,  crm.HEADERS)


def update_customer(): 
    new_customer = manager.read_table_from_file(crm.DATAFILE)
    id = view.get_input("Customer id you want to update: ")
    print()
    for customer in new_customer:
        if id == customer[0]:
            updated_name = view.get_input("New Name: ")
            print()
            updated_email = view.get_input("New Email: ")
            print()
            updated_subscribed = view.get_input("Subscribed? ")
            while updated_subscribed.lower() != 'yes' and updated_subscribed.lower() != 'no':
                updated_subscribed = view.get_input("Subscribed? yes or no ")
            if updated_subscribed == "yes":
                updated_subscribed = "1"
            elif updated_subscribed == "no":
                updated_subscribed = "0"
            customer[1] = updated_name
            customer[2] = updated_email
            customer[3] = updated_subscribed
            print(customer)
    manager.write_table_to_file(crm.DATAFILE, new_customer)
    view.print_table(new_customer,  crm.HEADERS)


def delete_customer():
    customers = manager.read_table_from_file(crm.DATAFILE)
    id = view.get_input('Customer id: ')
    for customer in customers:
        if customer[0] == id:
            customers.remove(customer)
            break
    manager.write_table_to_file(crm.DATAFILE, customers)
    view.print_table(customers,  crm.HEADERS)
    

def get_subscribed_emails():  
    customers = manager.read_table_from_file(crm.DATAFILE)
    subscribed = [customer for customer in customers if customer[3] == '1']
    view.print_table(subscribed, crm.HEADERS)
    

def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu(f"{Fore.GREEN}\nCustomer Relationship Management\n{Style.RESET_ALL}", options)


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