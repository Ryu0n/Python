import copy

n = int(input())

def p(lis):
    print(' '.join(map(str, lis)))

row = [1]
for i in range(n):
    if i == 0:
        p(row)
    elif i == 1:
        row = [1, 1]
        p(row)
    else:
        dish = copy.deepcopy(row)
        for j in range(len(dish) - 1):
            row[j + 1] = dish[j] + dish[j + 1]
        row.append(1)
        p(row)