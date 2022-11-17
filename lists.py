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
my_elem = l2[3]
print(my_elem)
print(my_elem[6:12])

#TODO Sum up all numbers in l2
# print('--------------')
# l2.remove('Hello Python 3')
# print(l2)
# #my_elem1=l2
# sum = sum(l2)
# print(sum)

print('--------------')
total_sum = 0
for item in l2:
    if type(item) is int:
        total_sum = total_sum + item
print(total_sum)
print(l2)

#l3 = [ x for x in l2 if type(x)==int]
l3 = [ x for x in l2 if isinstance(x, (int, float, complex))]
print(l3)
print(sum(l3))
