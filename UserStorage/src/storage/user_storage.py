from .user import User
import fnmatch

class UserStorage:

    def __init__(self):
        self.storage = []
    
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
    
    def get_all_users(self):
        return self.storage
    
    def clear_users(self):
        self.storage.clear()    