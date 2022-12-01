import io
import os

my_folder = r'c:\users\prubac\Desktop'

my_file_location = r'..\hello.txt'


my_file = os.path.join(my_folder, my_file_location)
print(os.path.dirname(my_file))
#print(os.path.exists(my_file))
if os.path.exists(my_file):
    print('{}: exists'.format(my_file))
else:
    print('{}: does not exist'.format(my_file))
print(my_file)
#my_file = r'H:\Python_Winter_2022_1\hello.txt'  # raw string - no special symbols
#my_file = 'H:\\Python_Winter_2022_1\\hello.txt'  # raw string - no special symbols
#my_file = 'H:/Python_Winter_2022_1/hello.txt'  # raw string - no special symbols

print('Current path: {}'.format(os.getcwd()))
print('Reading file from: {}'.format(os.path.abspath(my_file)))


# f = open(my_file, 'r')
# lines = f.readlines()
# i = 0
# for line in lines:
#     i += 1
#     print(f'{i}: {line}', end='')
# f.close()


with open(my_file, 'r') as f:
    lines = f.readlines()
    print(lines)
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')
