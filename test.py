import utils.file_operations

string='John'
utils.file_operations.save_to_file(string,'data.txt')

print(utils.file_operations.read_to_file('data.txt'))