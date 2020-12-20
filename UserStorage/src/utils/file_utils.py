def read_file_contents(file_path):
    file = open(file_path)
    contents = file.read()
    file.close()
    return contents

def write_contents_to_file(file_path, contents):
    file = open(file_path, 'w')
    file.write(contents)
    file.close()