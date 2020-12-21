from .raw_formatter import RawFormatter
from .table_formatter import TableFormatter

class Formatter():

    def __init__(self):
        self.formatters = {
            'raw' : RawFormatter(),
            'table' : TableFormatter()
        }

    def format_data(self, data, headers, data_format):
        result = ''
        if self.is_supported(data_format):
            processed = []
            for value in data:
                processed.append(value.to_array())
            result = self.formatters[data_format].format(processed, headers)
        return result

    def is_supported(self, data_format):
        return self.formatters.get(data_format)

    def get_supported_formats(self):
        formats = []
        for fmt in self.formatters:
            formats.append(fmt)
        return formats