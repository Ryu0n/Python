#n = 73425
n = 10007
#n = 9

import copy

answer = [0, 0]

def solution(n):
    if len(str(n)) != 1:
        if len(str(n)) % 2 != 0:
            n = str(n)

            split_1 = 0; split_2 = 0;

            startPoint_1 = int(len(str(n)) / 2) # 2
            startPoint_2 = startPoint_1 + 1 # 3

            while n[startPoint_1:][0] == '0':
                startPoint_1 += 1

            while n[startPoint_2:][0] == '0':
                startPoint_2 += 1

            print('1 : ', n[:startPoint_1], n[startPoint_1:])
            print('2 : ', n[:startPoint_2], n[startPoint_2:])

            if int(n[:startPoint_1]) + int(n[startPoint_1:]) > int(n[:startPoint_2]) + int(n[startPoint_2:]):
                split_1 = int(n[:startPoint_2])
                split_2 = int(n[startPoint_2:])
            else:
                split_1 = int(n[:startPoint_1])
                split_2 = int(n[startPoint_1:])

            n = split_1 + split_2

            print(n)

        else:
            n = str(n)

            startPoint = int(len(str(n)) / 2)

            while n[startPoint:][0] == '0':
                startPoint += 1

            split_1 = int(n[:startPoint])
            split_2 = int(n[startPoint:])

            n = split_1 + split_2

        answer[0] += 1
        answer[1] = n
    answer[1] = n
    if len(str(n)) == 1:
        a = copy.deepcopy(answer)
        return a

    b = solution(n)
    return b


print(solution(n))