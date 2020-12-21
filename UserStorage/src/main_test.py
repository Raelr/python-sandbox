import unittest
import utils.file_utils as utils
import os
from storage.user_storage import UserStorage
from serialisation.serialiser import Serialiser
from formatting.formatter import Formatter

class TestUserStorage(unittest.TestCase):

    # MAIN TESTS:
    
    # Test basic addomg and searching for users with glob syntax
    def test_basic_search(self):
        user_storage = UserStorage()

        user_storage.add_user('Robert Oppenheimer', 'Nuclear Street', 124546454343)

        name_results = user_storage.filter_users("*Name:Robert Oppenheimer*")
        address_results = user_storage.filter_users("*Address: Nuclear Street*")
        phone_results = user_storage.filter_users("*Phone: 124546454343*")

        self.assertGreater(len(name_results), 0)
        self.assertGreater(len(address_results), 0)
        self.assertGreater(len(phone_results), 0)
    
    # Test some glob widlcards to make sure they work
    def test_wildcard_search(self):
        user_storage = UserStorage()

        self.populate_storage(user_storage)

        albert_search_results = user_storage.filter_users("*Name:Albert*", )
        address_search_results = user_storage.filter_users("*Street*")
        phone_search_results = user_storage.filter_users("*Phone:[1,2]24*")

        self.assertEqual(len(albert_search_results), 2)
        self.assertEqual(len(address_search_results), 2)
        self.assertEqual(len(phone_search_results), 2)

    # Test serialisation to both JSON and YAML
    def test_saving_files_json(self):
        user_storage = UserStorage()
        serialiser = Serialiser()

        self.populate_storage(user_storage)

        self.save_and_test('json', user_storage, serialiser)

        self.save_and_test('yaml', user_storage, serialiser)

    # Test de-serialisation from JSON and YAML
    def test_loading_files(self):
        user_storage = UserStorage()
        serialiser = Serialiser()

        self.populate_storage(user_storage)

        self.save_and_load_file('json', user_storage, serialiser)

        self.save_and_load_file('yaml', user_storage, serialiser)

    # Tests to see that storage formats are being fount here. 
    def test_get_supported_formats(self):
        serialiser = Serialiser()
        formatter = Formatter()

        self.assertNotEqual(serialiser.get_supported_formats(), '')
        self.assertNotEqual(formatter.get_supported_formats(), '')
    
    # UTILITY FUNCTIONS:

    # Re-usable method for saving and validating that a file was created
    def save_and_test(self, file_format, user_storage, serialiser):
        data = serialiser.serialise(user_storage.get_all_users(), file_format)
        utils.write_contents_to_file("../data/user_storage." + file_format, data)

        self.assertEqual(os.path.exists('../data/user_storage.' + file_format), True)

        os.remove('../data/user_storage.' + file_format)
        
    # Re-usable method for serialising and de-serialising the user data
    def save_and_load_file(self, file_format, user_storage, serialiser):
        data = serialiser.serialise(user_storage.get_all_users(), file_format)
        utils.write_contents_to_file("../data/user_storage." + file_format, data)

        user_storage.clear_users()

        self.assertEqual(len(user_storage.storage), 0)

        users = serialiser.deserialise(utils.read_file_contents('../data/user_storage.' + file_format), file_format)
        for val in users:
            user_storage.add_user(val['name'], val['address'], val['phone_number'])

        self.assertGreater(len(user_storage.storage), 0)
    
    # Re-usable method that populates a storage object with some pre-made data
    def populate_storage(self, storage):
        storage.add_user('Robert Oppenheimer', 'Nuclear Street', 124546454343)
        storage.add_user('Albert Einstein', 'Light Avenue', 1243243545443)
        storage.add_user('Albert Brown', 'Brown Street', 654232412535425)

unittest.main()