import json

class JSONSerialiser():

    def __init__(self):
        pass
    
    def serialise(self, users):
        return json.dumps([user.__dict__ for user in users], indent=4)

    def deserialise(self, string):
        return json.loads(string)