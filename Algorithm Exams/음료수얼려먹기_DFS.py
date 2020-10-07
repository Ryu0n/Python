# 이 문제는 DFS BFS 둘 다 풀수 있습니다.
answer = 0

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def dfs(ver, hor):
    # 현재 위치가 범위를 벗어나면 무시
    if ver < 0 or ver >= N or hor < 0 or hor >= M:
        return False

    # 해당 노드가 방문한 적이 없으면
    if graph[ver][hor] == 0:
        # 해당 노드를 방문 처리하고
        graph[ver][hor] = 1
        # 인접 노드로 이동한다. (상, 하, 좌, 우)
        dfs(ver - 1, hor)
        dfs(ver + 1, hor)
        dfs(ver, hor - 1)
        dfs(ver, hor + 1)
        return True
    return False

# 모든 점을 순회한다.
# 한 점으로부터 DFS 방식으로 해당하는 영역에 전부 방문 처리를 한다.
# 다음 점으로 넘어가도 이미 전의 점에서 해당하는 영역에 방문 처리를 했으므로 더이상 검사하지 않는다.
for ver in range(len(graph)):
    for hor in range(len(graph[ver])):
        if dfs(ver, hor) == True:
          answer += 1

print(answer)

