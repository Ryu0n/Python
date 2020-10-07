import copy

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


def dfs_turnoff(ver, hor):
    if ver < 0 or ver >= M or hor < 0 or hor >= N:
        return False

    if graph_turnoff[ver][hor] == 1:
        graph_turnoff[ver][hor] = 0
        dfs_turnoff(ver - 1, hor)
        dfs_turnoff(ver + 1, hor)
        dfs_turnoff(ver, hor - 1)
        dfs_turnoff(ver, hor + 1)
        return True

    return False

answer_turnon = 0
answer_turnoff = 0

M, N = map(int, input().split())

graph_turnon = []
graph_turnoff = []

for i in range(M):
    graph_turnon.append(list(map(int, input().split())))

graph_turnoff = copy.deepcopy(graph_turnon)

for ver in range(len(graph_turnon)):
    for hor in range(len(graph_turnon[ver])):
        if dfs_turnon(ver, hor) == True:
            answer_turnon += 1


for ver in range(len(graph_turnoff)):
    for hor in range(len(graph_turnoff[ver])):
        if dfs_turnoff(ver, hor) == True:
            answer_turnoff += 1


print(answer_turnon, answer_turnoff)
