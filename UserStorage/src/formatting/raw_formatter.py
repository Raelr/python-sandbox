# ------------------------------------------ RAWFORMATTER.PY --------------------------------------------- #
# A very simple class for handling a specific formatting case. In this case, this class formats            #
#  data to a custom raw format and returns a string.                                                       #
# -------------------------------------------------------------------------------------------------------- #

class RawFormatter():

    # Constructor
    def __init__(self):
        pass
    
    # Formats a single attribute via the headers provided
    def get_attribute(self, attribute, data):
        return '{0}: {1}'.format(attribute, data)

    # Formats the string
    def format(self, data, headers):
        result = ''

        attributes = []
        
        # iterate over all the data and re-format it
        for collection in data:
            value = ''
            for i in range(len(collection)):   
                value += self.get_attribute(headers[i], collection[i]) + ', '
            attributes.append(value)

        for i in range(len(attributes)):
            result += '\t {0}. {1} \n'.format(str(i), attributes[i])

        return 'QUERY RESULTS:\n\n[\n {0}]'.format(result)


