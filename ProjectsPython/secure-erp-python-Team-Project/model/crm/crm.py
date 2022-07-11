""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""


from model.data_manager import read_table_from_file

DATAFILE = "model/crm/crm.csv"
HEADERS = ["ID", "NAME", "EMAIL", "SUBSCRIBED"] 


crm_list = (read_table_from_file(DATAFILE, separator=';'))
