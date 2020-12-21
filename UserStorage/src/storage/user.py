class User():
    name = ""
    address = ""
    phone_number = 0

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return 'Name: {0} | Address: {1} | Phone: {2}'.format(self.name, self.address, self.phone_number)
    
    def __repr__(self):
        return str(self)

    def equals(self, other):
        return self.name == other.name and self.address == other.address and self.phone_number == other.phone_number
    
    def to_array(self):
        return [self.name, self.address, self.phone_number]