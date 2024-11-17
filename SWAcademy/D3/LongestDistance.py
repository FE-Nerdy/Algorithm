def dfs(v, cnt):
    global max_count

    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, cnt+1)
    visited[v] = False

    if cnt > max_count:
        max_count = cnt

T = int(input())

for tc in range (1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    visited = [False] * (n+1)

    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    cnt, max_count = 0,0

    for i in range(1, n+1):
        dfs(i, 1)

    print(f'#{tc} {max_count}')