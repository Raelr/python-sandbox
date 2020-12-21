# ----------------------------------------- TABLEFORMATTER.PY -------------------------------------------- #
# A very simple class for handling a specific formatting case. In this case, this class formats            #
#  data to a table and returns a string.                                                                   #
# -------------------------------------------------------------------------------------------------------- #

from tabulate import tabulate

class TableFormatter():

    # Constructor
    def __init__(self):
        pass
    
    # Formats the string to a table and returns the result
    def format(self, data, headers):
        return tabulate(data, headers, tablefmt='fancy_grid')