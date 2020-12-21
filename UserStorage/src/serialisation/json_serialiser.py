# ------------------------------------------ JSONSERIALISER.PY ------------------------------------------- #
# A very simple class for handling a specific serialisation case. In this case, this class serialises      #
# and deserialises data to JSON and returns the string.                                                    #
# -------------------------------------------------------------------------------------------------------- #

import json

class JSONSerialiser():

    # Constructor
    def __init__(self):
        pass
    
    # Takes an array of data and serialises the contents
    def serialise(self, data):
        return json.dumps([value.__dict__ for value in data], indent=4)

    # De-serialises a JSON string into component parts 
    def deserialise(self, string):
        return json.loads(string)