# ------------------------------------------------ APP.PY ------------------------------------------------ #
# This is where the user storage API is put into action!                                                   #
# This is a simple CLI application which allows users to add and filter users, serialise and de-serialise  #
# users to json or yaml, and formats returned data in either a raw or table format. All available          #
# options can be found in the show_menu() function.                                                        #
# -------------------------------------------------------------------------------------------------------- #

from user_storage import UserStorage

class App():

    # Simple constructor for the CLI Application
    def __init__(self):
        self.storage = UserStorage()
        self.running = True
    
    # Runs the main loop for the application
    def run(self):
        print('\nWELCOME TO THE USER MANAGER APP!\n')
        self.show_menu()
        try: 
            while self.running:
                self.process_menu_options()
        except (KeyboardInterrupt):
            print('Keyboard Interrupted, closing application!')
        except Exception as e:
            print('An exception has occurred: ', e.__class__, '. Closing Application.')

    # Display the menu options
    def show_menu(self):
        print('\nWhat would you like to do?')
        print('1. Add User.')
        print('2. Filter Users')
        print('3. Save Users')
        print('4. Load Users')
        print('5. Show Available Formats')
        print('6. Show Options')
        print('7. Exit')
        print('(Please choose a number between 1 and 6)\n')
    
    # Processes user input and translates it into decisions:
    def process_menu_options(self):
        # Get the user's menu choice
        user_input = self.get_user_input('What would you like to do? ')

        if user_input == '1':
            self.add_user()
        elif user_input == '2':
            self.filter_users()
        elif user_input == '3':
            self.save_users()
        elif user_input == '4':
            self.load_users()
        elif user_input == '5':
            self.show_formats()
        elif user_input == '6':
            self.show_menu()
        elif user_input == '7':
            self.running = False
        else:
            self.show_menu()

    # Helper method for getting user input and returning it
    def get_user_input(self, message):
        return input(message)
    
    # Asks for user information and adds it to storage
    def add_user(self):
        # Get all the attributes for users
        name = self.get_user_input('What is the user\'s name? ')
        address = self.get_user_input('What is the user\'s address? ')
        phone = int(self.get_user_input('What is the user\'s phone number? (No spaces, please!) '))

        print('Adding user: {0} with address: {1} and phone number: {2}...'.format(name, address, phone))
        # Confirm that the user is OK with the data entered. 
        if self.is_user_confirmed():
            # Add the new user! 
            self.storage.add_user(name, address, phone)

    # Method for handling user filter commands. Uses a Glob search to find users. 
    def filter_users(self):
        # Get the user's query and desired data format
        filter_command = self.get_user_input('What Glob rules would you like to apply? ')
        format_type = self.get_user_input('What format would you like the data formatted in (json, yaml, raw, table)? ')

        # Get the user list and format according to the user's specification:
        print(self.storage.format_result(format_type, self.storage.filter_users(filter_command)))

    # Method for handling user saving to json or yaml
    def save_users(self):
        # Get the format we want to serialise the data to:
        data_format = self.get_user_input('What format would you like the data saved to (json or yaml)? ')
        
        # Save the user
        self.storage.save_users(data_format)
        print('Saving Data to ' + data_format + ' format')
    
    # Method for handling user loading from json or yaml
    def load_users(self):
        # Get the format we want to de-serialise the data from:
        data_format = self.get_user_input('What format would you like the to be loaded from (json or yaml)? ')
        
        # Load the stored users
        self.storage.load_users(data_format)
        print('Loaded Data from ' + data_format + ' source!')
    
    # Method for returning and printing 
    def show_formats(self):
        print(self.storage.get_supported_formats())
    
    # Helper method for confirming user input (used for verifying their intent)
    def is_user_confirmed(self):
        # Get user confirmation
        user_input = self.get_user_input('Are you sure sure you want to proceed (y/n)? ')
        
        # Fail unless user inputs y
        should_continue = False

        if user_input == 'y' or user_input == 'Y':
            should_continue = True
        else:
            print('Returning to menu...')
        
        return should_continue