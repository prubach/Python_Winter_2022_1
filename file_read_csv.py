my_file = 'my_matrix.csv'
m = []
with open(my_file, 'r') as f:
    lines = f.readlines()
    print(lines)
    i = 0
    s = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')
        cells = line.split(';')
        r = []
        for c in cells:
            s += int(c)
            r.append(int(c))
            print(f'c:{c}')
        m.append(r)

print(s)
print(m)

# Writing...

my_file = 'my_matrix_out.csv'
#m = []
with open(my_file, 'a') as f:
    for r in m:
        l = ';'.join([str(e) for e in r])
        f.write(l + '\n')
