my_file = 'hello.txt'

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
