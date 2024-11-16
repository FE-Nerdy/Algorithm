T = int(input())

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    li = [[0] * N for _ in range(N)]
    x, y = 0, 0
    d = 0

    for i in range(1, N * N + 1):
        li[x][y] = i

        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and li[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x, y = x + dx[d], y + dy[d]
    print(f"#{tc}")
    for row in li:
        print(" ".join(map(str, row)))
