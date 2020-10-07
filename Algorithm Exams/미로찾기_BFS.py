from collections import deque
import pprint

def bfs(x, y):
    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            # 노드의 값이 1일 경우에만 덮어씌우므로
            # 만약 경로가 여러개 일 경우 최단경로가 목적지에 도달하여
            # 이미 값을 덮어씌웠을 것이므로
            # 그 후에 도착한 경로들의 값은 등록되지 않는다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    return graph[N - 1][M - 1]




N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

# UP, DOWN, LEFT, RIGHT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))