import os

my_folder = r'c:\users\prubac\Desktop'
print(os.listdir(my_folder))
for f in os.listdir(my_folder):
    print('{}: {}'.format(f, os.path.isdir(f)))