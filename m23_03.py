file_path = 'registrations.txt'

with open(file_path, 'r', encoding='UTF-8') as input_file:
    line_list = input_file.readline().split()

print(line_list)
