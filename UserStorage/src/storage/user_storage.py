# ----------------------------------------- USERSTORAGE.PY ----------------------------------------------- #
# This is the class that stores all of our user storage logic.                                             #
# The supported operations are: add_user(), search_user(), filter_users(), get_all_users(), and            #
# clear_users()                                                                                            #
# -------------------------------------------------------------------------------------------------------- #

from .user import User
import fnmatch

class UserStorage:
    
    # Constructor
    def __init__(self):
        self.storage = []
    
    # Adds a user to the storage array
    def add_user(self, name, address, phone):
        user = User(name, address, phone)
        if not self.search_user(user):
            self.storage.append(user)

    # Searches the storage array for a specified user
    def search_user(self, user):
        is_found = False
        for stored_user in self.storage:
            # .equals() is a helper function that (hopefully) the given data will implement. 
            if stored_user.equals(user):
                is_found = True
        return is_found
    
    # Uses Glob syntax to retun an array of users
    def filter_users(self, command):
        results = []
        
        for user in self.storage:
            if fnmatch.fnmatch(str(user).replace(" ", ""), command.replace(" ","")):
                results.append(user)

        return results if len(results) > 0 else 'No matching entry found!'
    
    # Returns the storage array
    def get_all_users(self):
        return self.storage
    
    # Clears the storage array
    def clear_users(self):
        self.storage.clear()    