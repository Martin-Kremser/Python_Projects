from model import data_manager as manager
from view import terminal as view
from model.sales import sales
from model import util
from colorama import Fore, Style
from view.terminal import clear_terminal


def list_transactions():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    view.print_table(transactions, sales.HEADERS)
    

def add_transaction():
    transaction = manager.read_table_from_file(sales.DATAFILE)
    data = view.get_inputs(sales.HEADERS[1:])
    data.insert(0, util.generate_id())
    transaction.append(data)
    manager.write_table_to_file(sales.DATAFILE, transaction)
    view.print_table(transaction, sales.HEADERS)


def update_transaction():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    view.print_table(transactions, sales.HEADERS)
    new_transaction = manager.read_table_from_file(sales.DATAFILE)
    id = view.get_input("Enter the ID of the transaction you want to update: ")
    print()
    for transaction in new_transaction:
        if id == transaction[0]:
            updated_customer = view.get_input("\nUpdate the name of the customer: ")
            updated_product = view.get_input("\nUpdate the name of the product: ")
            updated_price = view.get_input("\nUpdate the price: ")
            updated_date = view.get_input("\nUpdate the date of the sale: ")
            transaction[1] = updated_customer
            transaction[2] = updated_product
            transaction[3] = updated_price
            transaction[4] = updated_date
            print(transaction)
    
    manager.write_table_to_file(sales.DATAFILE, new_transaction)
    view.print_table(new_transaction, sales.HEADERS)
 

def delete_transaction():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    view.print_table(transactions, sales.HEADERS)
    id = view.get_input("Enter transaction id to remove the transaction from the list: ")
    for transaction in transactions:
        if transaction[0] == id:
            transactions.remove(transaction)
            break
    manager.write_table_to_file(sales.DATAFILE, transactions)
    view.print_table(transactions, sales.HEADERS)
 

def get_biggest_revenue_transaction():
    clear_terminal()
    income = []
    transactions = manager.read_table_from_file(sales.DATAFILE)
    for transaction in transactions:
        income.append(float(transaction[3]))
    max_income_index = income.index(max(income))
    #print(income)
    #print("max income index", max_income_index)
    id_max_income_transaction = transactions[max_income_index][0]
    print(f"\nThe transaction that generated the single highest revenue of {max(income)} money units is {transactions[max_income_index][2]} and the sales id is {id_max_income_transaction}.\n")
 

def get_biggest_revenue_product():
    clear_terminal()
    transactions = manager.read_table_from_file(sales.DATAFILE)
    product_price_dict = {}
    for id, customer, product, price, date in transactions:
        if product in product_price_dict.keys():
            product_price_dict[product] += float(price)
        else:
            product_price_dict[product] = float(price)
    # sorting dictionary after values
    VALUES = 1
    list_of_tupples = sorted(product_price_dict.items(), key=lambda x: x[VALUES])
    product, biggest_revenue = list_of_tupples[-1]  # the last is the biggest
    biggest_revenue = "{:.2f}".format(biggest_revenue)
    print(f"The product with the highest revenue is {product}\nand the total revenue amounts to {biggest_revenue} money units. ")
 

def count_transactions_between():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    print("Please provide the initial and final dates between which you would like to know the number of transactions made: ")
    initial_date = view.get_input("Date in format yyyy-mm-dd ")
    final_date = view.get_input("Date in format yyyy-mm-dd ")
    transaction_count = 0
    for id, customer, product, price, date in transactions:
        if initial_date <= date <= final_date:
            transaction_count += 1
    list_transactions()
    print(f"The number of transactions between {initial_date} and {final_date} amounts to {transaction_count} business cases. ")
 

def sum_transactions_between():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    print("Please provide the initial and final dates between which you would like to know the total sum of revenue made: ")
    initial_date = view.get_input("Date in format yyyy-mm-dd ")
    final_date = view.get_input("Date in format yyyy-mm-dd ")
    transaction_sum = 0
    for id, customer, product, price, date in transactions:
        if initial_date <= date <= final_date:
            transaction_sum += float(price)
    list_transactions()
    formated_transaction_sum = "{:10.2f}".format(transaction_sum)
    print(f"The total sum for all transactions made between {initial_date} and {final_date} is {formated_transaction_sum} money units. ")
  

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu(f"{Fore.GREEN}\nSales\n{Style.RESET_ALL}", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("\nSelect an operation ")
            print()
            run_operation(int(operation))
            print()
        except KeyError as err:
            view.print_error_message(err)
    else:
        clear_terminal()