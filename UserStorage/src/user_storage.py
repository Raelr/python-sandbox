from user import User
from serialisation.serialiser import Serialiser
from formatting.formatter import Formatter
from tabulate import tabulate
import utils.file_utils as utils
import fnmatch

class UserStorage:

    def __init__(self):
        self.storage = []
        self.serialiser = Serialiser()
        self.formatter = Formatter()
    
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
        string = self.serialiser.serialise(self.storage, file_type)
        utils.write_contents_to_file("../data/user_storage." + file_type, string)
    
    def load_users(self, file_type):
        users = self.serialiser.deserialise(utils.read_file_contents('../data/user_storage.' + file_type), file_type)
        for val in users:
            self.add_user(val['name'], val['address'], val['phone_number'])
    
    def clear_users(self):
        self.storage.clear()
    
    def format_result(self, result_format, data):
        result_str = ''

        if self.formatter.is_supported(result_format):
            result_str = self.formatter.format_data(data,['Name','Address','Phone'], result_format)
        elif self.serialiser.is_supported(result_format):
            result_str = self.serialiser.serialise(data, result_format)
        else:
            result_str = 'ERROR: support for format: ' + result_format + ' does not exist!'

        return '\n' + result_str + '\n'
    
    def get_supported_formats(self):
        format_list = ''

        format_list += '\nData Formats Supported: \n'
        format_list += self.format_list(self.formatter.get_supported_formats())
        format_list += self.format_list(self.serialiser.get_supported_formats())

        return format_list
    
    def format_list(self, collection):
        result = ''
        if len(collection) > 0:
            for formatter in collection:
                result += '   - {0}\n'.format(formatter)
        return result
        
        