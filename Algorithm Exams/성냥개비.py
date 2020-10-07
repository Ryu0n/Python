from itertools import permutations

condition =[0] * 10

condition[0] = '6'
condition[1] = '2'
condition[2] = '5'
condition[3] = '5'
condition[4] = '4'
condition[5] = '5'
condition[6] = '6'
condition[7] = '3'
condition[8] = '7'
condition[9] = '6'

for i in range(1, 11):
    per = permutations(condition, i)
    print(list(map(' '.join, per)))