from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller
from colorama import Fore, Style
import os
from view.terminal import clear_terminal


os.system('cls' if os.name == 'nt' else 'clear')


def load_module(option):
    if option == 1:
        clear_terminal()
        crm_controller.menu()
    elif option == 2:
        clear_terminal()
        sales_controller.menu()
    elif option == 3:
        clear_terminal()
        hr_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    print()
    print(f"{Fore.CYAN}WELCOME TO THE SECURE ERP APPLICATION!{Style.RESET_ALL}")
    print()
    options = ["Exit program",
               "Customer Relationship Management (CRM)",
               "Sales",
               "Human Resources"]

    view.print_menu(" <<< Main menu >>>\n", options)


def menu():
    option = None
    while option != '0':
        display_menu()
        try:
            option = view.get_input("\nSelect module ")
            load_module(int(option))
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!")
    print("\nGOOD-BYE!")
