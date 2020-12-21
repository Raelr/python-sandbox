# --------------------------------------------- FORMATTER.PY --------------------------------------------- #
# A module that handles all data formatting. This module's intent is to dynamically handle list and result #
# strig formatting. Currently, the module can handle table and raw formatting.                             #
# -------------------------------------------------------------------------------------------------------- #

from .raw_formatter import RawFormatter
from .table_formatter import TableFormatter

class Formatter():

    # Constructor
    def __init__(self):
        self.formatters = {
            'raw' : RawFormatter(),
            'table' : TableFormatter()
        }

    # Formats data in a specified format. Currently supports either Table or Raw formats.
    def format_data(self, data, headers, data_format):
        result = ''
        if self.is_supported(data_format):
            processed = []
            for value in data:
                processed.append(value.to_array())
            result = self.formatters[data_format].format(processed, headers)
        return result

    # Returns True if a given format is supported.
    def is_supported(self, data_format):
        return self.formatters.get(data_format)

    # Returns all supported formats
    def get_supported_formats(self):
        formats = []
        for fmt in self.formatters:
            formats.append(fmt)
        return formats
    
    # Takes a list of strings and formats them in a more readable format.
    def format_list(self, data):
        result = ''
        if len(data) > 0:
            for value in data:
                result += '   - {0}\n'.format(value)
        return result