def save_to_file(userstring, filename):
    with open(filename,'w') as file:
        file.write(userstring)



def read_to_file(filename):
    with open(filename, 'r') as file:
        return file.read().split('\n')


