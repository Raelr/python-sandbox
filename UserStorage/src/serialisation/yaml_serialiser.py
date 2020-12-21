# ------------------------------------------ YAMLSERIALISER.PY ------------------------------------------- #
# A very simple class for handling a specific serialisation case. In this case, this class serialises      #
# and deserialises data to YAML and returns the string.                                                    #
# -------------------------------------------------------------------------------------------------------- #

import yaml 

class YAMLSerialiser():

    # Constructor
    def __init__(self):
        pass
    
    # Serlialises data in an array to YAML
    def serialise(self, data):
        return yaml.dump([value.__dict__ for value in data], sort_keys=False, indent=4)

    # De-serialises a yaml string to component parts
    def deserialise(self, string):
        return yaml.safe_load(string)