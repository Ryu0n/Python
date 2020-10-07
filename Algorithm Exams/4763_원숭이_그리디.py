import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 미해결
if __name__ == '__main__':
    monkeyNum = int(input())

    monkeys = []

    cage_1 = []
    cage_2 = []

    # 인접리스트 생성
    for i in range(0, monkeyNum):
        enemyInfo = [0] * monkeyNum
        monkeys.append(enemyInfo)
    print(monkeys)

    # 앙숙관계 정보 입력
    info = []
    for monkey in range(0, monkeyNum):
        enemyInfo = input().split(' ')
        enemyInfo = list(map(int, enemyInfo))
        for i in range(1, len(enemyInfo)):
            enemyInfo[i] -= 1
        info.append(enemyInfo[1:len(enemyInfo)])
    print(info)

    # 앙숙관계를 인접리스트로 변환
    for j in range(0, len(info)):
        for k in range(0, len(info[j])):
            monkeys[j][info[j][k]] = 1
    print(monkeys)

    # for a in range(0, len(monkeys)):
    #     for b in range(0, len(monkeys)):
    #         if monkeys[a][b] == 0:
