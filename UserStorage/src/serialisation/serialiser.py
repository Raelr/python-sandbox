from .json_serialiser import JSONSerialiser
from .yaml_serialiser import YAMLSerialiser

class Serialiser():

    def __init__(self):
        self.serialisers = {
            'json' : JSONSerialiser(),
            'yaml' : YAMLSerialiser()
        }

    def serialise(self, data, data_format):
        result = ''
        if self.is_supported(data_format):
            result = self.serialisers[data_format].serialise(data)
        return result

    def deserialise(self, data, data_format):
        result = ''
        if self.is_supported(data_format):
            result = self.serialisers[data_format].deserialise(data)
        return result

    def get_supported_formats(self):
        serialisers = []
        for serialiser in self.serialisers:
            serialisers.append(serialiser)
        return serialisers
    
    def is_supported(self, data_format):
        return self.serialisers.get(data_format)