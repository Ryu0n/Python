def hanoi(N, start, end, sup):
    if N == 1:
        print(N, ' : ', start , '->', end)
        return
    hanoi(N - 1, start, sup, end) # N - 1번째 원반을 보조로 옮겨놓는다.
    print(N, ' : ', start, '->', end)
    hanoi(N - 1, sup, end, start) # 보조로 옮겨놨던 N - 1번째 원반을 목표로 옮긴다.

hanoi(2, 'A', 'C', 'B')