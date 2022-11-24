# Writing...
import json

my_file = 'my_matrix.json'
with open(my_file, 'r') as f:
    m = json.load(f)

print(type(m[0][1]))
print(m)
