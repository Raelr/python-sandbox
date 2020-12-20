from tabulate import tabulate

class TableFormatter():
    def __init__(self):
        pass
    
    def format(self, data, headers = None):
        return tabulate(data, headers, tablefmt='fancy_grid')