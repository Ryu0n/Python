from collections import deque

answer = 0

def bfs(ver, hor):
    global answer
    answer += 1

    # 해당 포인트의 좌표 정보를 노드로써 삽입합니다.
    queue = deque([[ver, hor]])

    # 최초의 노드를 방문 처리하고
    graph[ver][hor] = 1

    while queue:
        # 최상단 노드를 큐에서 꺼냅니다.
        node = queue.popleft()

        # 해당 노드의 인접 노드들의 좌표를 반환합니다.
        u_ver, u_hor = node[0] - 1, node[1]
        d_ver, d_hor = node[0] + 1, node[1]
        l_ver, l_hor = node[0], node[1] - 1
        r_ver, r_hor = node[0], node[1] + 1

        # 인접 노드들중 범위가 벗어나지 않고 방문한적이 없는 경우에 한해 큐에 추가하고 방문 처리합니다.
        if u_ver >= 0 and graph[u_ver][u_hor] == 0:
            queue.append([u_ver, u_hor])
            graph[u_ver][u_hor] = 1
        if d_ver < N and graph[d_ver][d_hor] == 0:
            queue.append([d_ver, d_hor])
            graph[d_ver][d_hor] = 1
        if l_hor >= 0 and graph[l_ver][l_hor] == 0:
            queue.append([l_ver, l_hor])
            graph[l_ver][l_hor] = 1
        if r_hor < M and graph[r_ver][r_hor] == 0:
            queue.append([r_ver, r_hor])
            graph[r_ver][r_hor] = 1

        # 한 영역에 대한 방문이 모두 끝났으므로 경우의 수를 증가합니다.
        # 고립된 경우 다른 영역으로 못넘어감
        # (주변 영역이 방문한 적 없는 경우에만 큐에 추가시키므로 모든 노드가 큐에서 pop이 되면 더 이상 이동할 곳이 없기 때문이다.)






# 이 문제는 DFS BFS 둘 다 풀수 있습니다.


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

for ver in range(len(graph)):
    for hor in range(len(graph[ver])):
        # 해당 포인트가 방문한 적이 없는 경우에만
        if graph[ver][hor] == 0:
            # BFS 알고리즘을 실행합니다.
            bfs(ver, hor)


print(answer)

