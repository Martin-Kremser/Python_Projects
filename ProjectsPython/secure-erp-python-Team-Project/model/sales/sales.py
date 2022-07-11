""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model.data_manager import read_table_from_file

DATAFILE = "model/sales/sales.csv"
HEADERS = ["ID", "CUSTOMER", "PRODUCT", "PRICE", "DATE"]


sales_list = (read_table_from_file(DATAFILE))