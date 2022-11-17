x1 = (244, 254)
print(x1)
print(x1[0])
y1 = (322, 363, 74674, 3472)
print(y1[1:3])
#y1[1]=6357
#print(y1)
print('---------')
d1 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March'}
print(d1.keys())
print(d1.values())

for k in d1.keys():
    print(f'{k}: {d1[k]}')

print('---------')
for k,v in d1.items():
    print(f'{k}: {v}')

#d2 = {}
d2 = d1
d2['Apr'] = 'April'
print(d2)

