# Writing...
import _pickle

my_file = 'my_matrix.dat'
with open(my_file, 'rb') as f:
    m = _pickle.load(f)

print(type(m[0][1]))
print(m)
