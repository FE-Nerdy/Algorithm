T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = []
    ans = 0

    for _ in range(N):
        li.append(list(map(int, input().split())))

    for col in range(N-M+1):
        for row in range(N-M+1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += li[col + k][row + l]
            ans = max(ans, tmp)
    print(f'#{tc} {ans}')