import yaml 

class YAMLSerialiser():

    def __init__(self):
        pass
    
    def serialise(self, users):
        return yaml.dump([user.__dict__ for user in users], sort_keys=False, indent=4)

    def deserialise(self, string):
        return yaml.safe_load(string)