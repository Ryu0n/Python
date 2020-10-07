def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

def fibo_topdown(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo_topdown(x - 1) + fibo_topdown(x - 2)
    return d[x]

def fibo_downtop(x):
    d[0] = 1
    d[1] = 1

    for c in range(2, x + 1):
        d[c] = d[c - 1] + d[c - 2]

    return d[x]

def ant_warrior():
    n = int(input())
    array = list(map(int, input().split()))

    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    print(d[n - 1])



def make_one():
    n = int(input())

    for i in range(2, n + 1):
        print(d)
        if i % 2 == 0:
            d[i] = min(d[i - 1], d[i // 2]) + 1
        if i % 3 == 0:
            d[i] = min(d[i - 1], d[i // 3]) + 1
        if i % 5 == 0:
            d[i] = min(d[i - 1], d[i // 5]) + 1
    print(d[n])

d = [0] * 100







def memorization_topdown(M):
    for m in money:
        print(cache)
        # 현재 잔액이 0원일 경우
        if M == 0:
            cache[M] = 0
            return 0

        # 범위를 벗어난 경우 (화폐로 조합이 불가능한 경우)
        if M < 0:
            return int(1e9)

        # 하위의 금액이 범위를 벗어나지 않으며 기록된 적이 있는 경우
        if M - m >= 0 and cache[M - m] != 1e9:
            cache[M] = min(cache[M], cache[M - m] + 1)
        # 그 밖의 경우
        else:
            cache[M] = min(cache[M], memorization_topdown(M - m) + 1)
    return cache[M]

def memorization_downtop():
    cache[0] = 0

    # 각 화폐에 대하여
    for i in range(N): 
        # 화폐의 가치부터 끝까지
        for j in range(money[i], M + 1):
            # 이전 기록이 존재하면 (만들 방법이 존재하면) - 0부터 시작하겠지?
            if cache[j - money[i]] != 1e9:
                # 이전 기록이랑 현재의 기록이랑 비교
                cache[j] = min(cache[j], cache[j - money[i]] + 1)

    if cache[M] == 1e9:
        print(-1)
    else:
        print(cache[M])




N, M = map(int, input().split())

cache = [int(1e9)] * (M + 1)

money = []

for i in range(N):
    money.append(int(input()))


# memorization_topdown(M)
# print(cache[M])
memorization_downtop()
