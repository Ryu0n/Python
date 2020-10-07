def dfs_turnon(ver, hor):
    if ver < 0 or ver >= M or hor < 0 or hor >= N:
        return False

    if graph_turnon[ver][hor] == 0:
        graph_turnon[ver][hor] = 1
        dfs_turnon(ver - 1, hor)
        dfs_turnon(ver + 1, hor)
        dfs_turnon(ver, hor - 1)
        dfs_turnon(ver, hor + 1)
        return True

    return False



answer_turnon = 0

M, N = map(int, input().split())

graph_turnon = []

for i in range(M):
    graph_turnon.append(list(map(int, input().split())))

for ver in range(len(graph_turnon)):
    for hor in range(len(graph_turnon[ver])):
        if dfs_turnon(ver, hor) == True:
            answer_turnon += 1

print(answer_turnon)
