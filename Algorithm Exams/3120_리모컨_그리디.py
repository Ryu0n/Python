import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def Nearest(list, value):
    nearest = 0
    minDistance = 40

    for num in list:
        if minDistance > abs(num - value):
            nearest = num
            minDistance = abs(num - value)

    return nearest

if __name__ == '__main__':
    deltas = [10, 5, 1, -1, -5, -10]

    count = 0

    temperature = input().split(' ')
    current = int(temperature[0])
    object = int(temperature[1])

    toMove = object - current

    while(toMove != 0):
        count+=1
        conditions = []
        for delta in deltas:
            conditions.append(toMove - delta)
        toMove = Nearest(conditions, 0)

    print(count)
