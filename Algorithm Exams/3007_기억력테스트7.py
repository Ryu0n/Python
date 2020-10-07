n, m = map(int, input().split())
num = list(map(int, input().split()))
num.insert(0, 0)

accumulate = []
for i in range(len(num)):
    if i == 0:
        accumulate.append(num[i])
    else:
        accumulate.append(accumulate[i - 1] + num[i])

infos = []
for i in range(m):
    infos.append(list(map(int, input().split(' '))))


for info in infos:
    print(accumulate[info[1]] - accumulate[info[0] - 1])