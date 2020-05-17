import utils.file_operations
#another options is   from utils.file_operations import save_to_file, read_to_file
#then we could call that function with   save_to_file or read_to_file command

from utils.find import find_in

string='John'
utils.file_operations.save_to_file(string,'data.txt')

print(utils.file_operations.read_to_file('data.txt'))