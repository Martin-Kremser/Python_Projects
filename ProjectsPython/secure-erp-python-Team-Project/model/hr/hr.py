""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model.data_manager import read_table_from_file

DATAFILE = "model/hr/hr.csv"
HEADERS = ["ID", "NAME", "DATE Of BIRTH", "DEPARTMENT", "CLEARANCE"]

hr_list = (read_table_from_file(DATAFILE))