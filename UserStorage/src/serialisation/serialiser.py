# ------------------------------------------ SERIALISER.PY ----------------------------------------------- #
# This module handles manages all the serialisation which the application can do. The module contains      #
# A dictionary of all existing format types. Currently, only YAML and JSON are supported.                  #
# -------------------------------------------------------------------------------------------------------- #

from .json_serialiser import JSONSerialiser
from .yaml_serialiser import YAMLSerialiser

class Serialiser():
    
    # Constructor
    def __init__(self):
        self.serialisers = {
            'json' : JSONSerialiser(),
            'yaml' : YAMLSerialiser()
        }

    # Handles all serialisation. Requires the user to input a format
    def serialise(self, data, data_format):
        result = ''
        if self.is_supported(data_format):
            result = self.serialisers[data_format].serialise(data)
        return result

    # De-serialises all provided data. Requires a data format to be specified. 
    def deserialise(self, data, data_format):
        result = ''
        if self.is_supported(data_format):
            result = self.serialisers[data_format].deserialise(data)
        return result

    # Returns a list of all supported formats.
    def get_supported_formats(self):
        serialisers = []
        for serialiser in self.serialisers:
            serialisers.append(serialiser)
        return serialisers
    
    # Simple function for checking if a given format is supported.
    def is_supported(self, data_format):
        return self.serialisers.get(data_format)