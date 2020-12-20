from user import User
from serialisation.json_serialiser import JSONSerialiser
from serialisation.yaml_serialiser import YAMLSerialiser
from formatting.table_formatter import TableFormatter
from formatting.raw_formatter import RawFormatter
import utils.file_utils as utils
import fnmatch
from tabulate import tabulate

class UserStorage:

    def __init__(self):
        self.storage = []
        self.serialisers = {
            'json' : JSONSerialiser(),
            'yaml' : YAMLSerialiser()
        }
        self.formatters = {
            'table' : TableFormatter(),
            'raw'   : RawFormatter()
        }
    
    def add_user(self, name, address, phone):
        user = User(name, address, phone)
        if not self.search_user(user):
            self.storage.append(user)

    def search_user(self, user):
        is_found = False
        for stored_user in self.storage:
            if stored_user.equals(user):
                is_found = True
        return is_found
    
    def filter_users(self, command):
        results = []
        for user in self.storage:
            if fnmatch.fnmatch(str(user).replace(" ", ""), command.replace(" ","")):
                results.append(user)

        return results if len(results) > 0 else 'No matching entry found!'
    
    def save_users(self, file_type):
        string = self.serialisers[file_type].serialise(self.storage)
        utils.write_contents_to_file("../data/user_storage." + file_type, string)
    
    def load_users(self, file_type):
        users = self.serialisers[file_type].deserialise(utils.read_file_contents('../data/user_storage.' + file_type))
        for val in users:
            self.add_user(val['name'], val['address'], val['phone_number'])
    
    def clear_users(self):
        self.storage.clear()
    
    def format_result(self, result_format, data):
        result_str = ''

        if self.formatters.get(result_format):
            format_data = []
            for user in data:
                format_data.append(user.to_array())
            result_str = self.formatters[result_format].format(format_data, ["Name", "Address", "Phone"])
        elif self.serialisers.get(result_format):
            result_str = self.serialisers[result_format].serialise(data)
        else:
            result_str = 'ERROR: support for format: ' + result_format + ' does not exist!'

        return '\n' + result_str + '\n'
    
    def get_supported_formats(self):
        format_list = ''
        
        if (len(self.formatters) > 0 or len(self.serialisers) > 0):
            format_list += '\nData Formats Supported: \n'
            format_list += self.format_list(self.formatters)
            format_list += self.format_list(self.serialisers)

        return format_list
    
    def format_list(self, collection):
        result = ''
        if len(collection) > 0:
            for formatter in collection:
                result += '   - {0}\n'.format(formatter)
        return result
        
        