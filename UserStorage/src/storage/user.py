# --------------------------------------------- USER.PY -------------------------------------------------- #
# This is the base User data structure.                                                                    #
# Each user in our application has three attributes: Name, Address, and Phone number.                      #
# -------------------------------------------------------------------------------------------------------- #

class User():

    # Constructor takes in the name, address, and phone number of the user
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    # Method to convert user to string
    def __str__(self):
        return 'Name: {0} | Address: {1} | Phone: {2}'.format(self.name, self.address, self.phone_number)
    
    # Allows us to print an array of users
    def __repr__(self):
        return str(self)

    # Helper function for comapring two users
    def equals(self, other):
        return self.name == other.name and self.address == other.address and self.phone_number == other.phone_number
    
    # Converts the user to an array (for formatting)
    def to_array(self):
        return [self.name, self.address, self.phone_number]