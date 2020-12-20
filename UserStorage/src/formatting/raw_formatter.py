class RawFormatter():
    def __init__(self):
        pass
    
    def get_attribute(self, attribute, data):
        return '{0}: {1}'.format(attribute, data)

    def format(self, data, headers):
        result = ''

        attributes = []
        for collection in data:
            value = ''
            for i in range(len(collection)):   
                value += self.get_attribute(headers[i], collection[i]) + ', '
            attributes.append(value)

        for i in range(len(attributes)):
            result += '\t {0}. {1} \n'.format(str(i), attributes[i])

        return 'QUERY RESULTS:\n\n[\n {0}]'.format(result)


