l_2d = [[24, 3, 36],
        [7, 3, 6],
        [7, 5, 8]]
print(l_2d[1][2])
in_list = l_2d[1]
print(in_list)
print(in_list[2])

#TODO - sum all values in columns

#TODO - sum all values in rows

sum_col = [0,0,0]
sum_row = [0,0,0]
for count1, ele1 in enumerate(l_2d):
    for count2, ele2 in enumerate(ele1):
        sum_row[count1] += ele2
        sum_col[count2] += ele2

print(f'Sum rows: {sum_row}')
print(f'Sum cols: {sum_col}')

#TODO - sum elements of the whole list
sum_all = 0
for i in l_2d:
    for j in i:
        sum_all += j

print(f'Sum all: {sum_all}')




