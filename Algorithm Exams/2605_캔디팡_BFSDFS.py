import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

SIZE_ROW = 7
SIZE_COL = 7

PANG = 0

def MoveTo(visited, board, y, x, pang):
    global PANG
    pang += 1
    visited[y][x] = 1
    color = board[y][x]
    # print(y, x, pang)

    if (pang == 3):
        # print('PANG')
        PANG += 1

    if (y - 1 > 0 and visited[y - 1][x] != 1):
        NextUpColor = board[y - 1][x]
        if (color == NextUpColor):
            # print('UP')
            pang = MoveTo(visited, board, y - 1, x, pang)

    if (y + 1 < SIZE_ROW and visited[y + 1][x] != 1):
        NextDownColor = board[y + 1][x]
        if (color == NextDownColor):
            # print('DOWN')
            pang = MoveTo(visited, board, y + 1, x, pang)

    if (x - 1 > 0 and visited[y][x - 1] != 1):
        NextLeftColor = board[y][x - 1]
        if (color == NextLeftColor):
            # print('LEFT')
            pang = MoveTo(visited, board, y, x - 1, pang)

    if (x + 1 < SIZE_COL and visited[y][x + 1] != 1):
        NextRightColor = board[y][x + 1]
        if (color == NextRightColor):
            # print('RIGHT')
            pang = MoveTo(visited, board, y, x + 1, pang)

    return pang

if __name__ == '__main__':
    board = []
    visited = []

    for row in range(0, SIZE_ROW):
        visited.append([0] * SIZE_COL)

    for row in range(0, SIZE_ROW):
        row = list(map(int, input().rstrip().split(' ')))
        board.append(row)

    # print(visited)
    # print(board)

    for y in range(0, SIZE_ROW):
        for x in range(0, SIZE_COL):
            MoveTo(visited, board, y, x, 0)
            # print()
    print(PANG)