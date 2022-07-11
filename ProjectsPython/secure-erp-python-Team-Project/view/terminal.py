from colorama import Fore, Style
import copy
import os


def clear_terminal(): 
    os.system('clear_terminal' if os.name == 'nt' else 'clear') 


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    count = -1
    for option in list_options:
        count += 1
        print(f'({count}) {option}', end='\n')


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int:
        print(f"{label}: {result}")
    elif type(result) == float:
        result_formatted = "{:.2f}".format(result)
        print(f"{label}: {result_formatted}")
    elif type(result) == list or type(result) == tuple:
        print(f"{label}:")
        print("; ".join(f"{e}" for e in result))
    elif type(result) == dict:
        print(f"{label}:")
        print("; ".join(f"{k}: {v}" for k, v in result.items()))
    print("")


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


def get_column_info(table, header):
    list_of_columns = []
    for column_index in range(len(header)):
        column_info = []
        for row in table:
            column_info.append(row[column_index])
        list_of_columns.append(column_info)
    return list_of_columns


def get_width_of_column(table, header):
    columns = get_column_info(table, header)
    list_of_widths = []
    for column in columns:
        maximum_length = max(column, key=len)
        list_of_widths.append(len(maximum_length))
    return list_of_widths


def print_table(table, header):
    clear_terminal()
    table = copy.deepcopy(table)
    print_header = copy.deepcopy(header)
    table.insert(0, print_header)
    widths = get_width_of_column(table, print_header)
    sum_of_widths = sum(widths)
    length_of_line = sum_of_widths + (7 * len(widths))
    line = f"{Fore.CYAN}•{'—' * length_of_line}•{Style.RESET_ALL}"
    line_2 = line.replace("•", "|")
    slash_beginning = f'{Fore.CYAN}|  {Style.RESET_ALL}'
    slash_end = f'{Fore.CYAN}   |{Style.RESET_ALL}'
    delimiter = f'{Fore.CYAN}   |   {Style.RESET_ALL}'
    line_header = f"{Fore.YELLOW}•{'—' * length_of_line}•{Style.RESET_ALL}"
    slash_beginning_header = f'{Fore.YELLOW}|  {Style.RESET_ALL}'
    slash_end_header = f'{Fore.YELLOW}   |{Style.RESET_ALL}'
    delimiter_header = f'{Fore.YELLOW}   |   {Style.RESET_ALL}'
    for index in range(len(print_header)):
        for i in table:
            if len(i[index]) == widths[index]:
                spacing_length = 0
                spacing1 = ""
                spacing2 = ""
            else:
                spacing_length = (widths[index] - len(i[index])) 
                spacing1 = (spacing_length//2) * " "
                if spacing_length % 2 == 0:
                    spacing2 = spacing1
                else:
                    spacing2 = len(spacing1) + 1
                    spacing2 *= " "
                i[index] = spacing1 + i[index] + spacing2
    print(line_header)
    for row in range(len(table)):
        if row == 0:
            print(slash_beginning_header, delimiter_header.join(table[row]), slash_end_header)
            print(line_header)
        elif row == len(table) - 1:
            print(slash_beginning, delimiter.join(table[row]), slash_end)
        else:
            print(slash_beginning, delimiter.join(table[row]), slash_end)
            print(line_2) 
    print(line)


def get_input(label):
    user_input = input(label)
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    list_with_new_inputs = []
    for i in labels:
        list_with_new_inputs.append(input(f'{i.upper()}: '))
        print()
    return list_with_new_inputs



def is_number(input_size):
    try:
        int(input_size)
        return True
    except ValueError:
        return False


""" def get_board_size():
    while True:
        board_size = input("\n How big do you want your board to be? (5-10)  ")
        if is_number(board_size):
            board_size = int(board_size)
            if 5 <= board_size <= 10:
                return board_size
            else:
                print(f"{Fore.RED}Invalid input! It must be a number between 5 and 10. Try again!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid input! That doesn't seem to be a number. Try again!{Style.RESET_ALL}") 
 """



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """

    print(f"{message}")
