l1 = [2525, 12536, 585895, 27848]
print(l1[1])
print(l1[1:3])

for i in range(len(l1)):
    print(f'el {i}={l1[i]}')

for val in l1:
    print(f'val={val}')

l1.append(2636)
print(l1)
l1.insert(1, 525623453)
print(l1)
l1.remove(27848)
print(l1)
l1.pop(1)
print(l1)
l1.sort()
l1.sort(reverse=True)
print(l1)


l2 = [2525, 12536, 585895, 'Hello Python 3', 27848]
#TODO Please extract the word "Python" from l2
#TODO Sum up all numbers in l2
