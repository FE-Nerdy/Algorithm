

for tc in range (1, 11):
    T = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    answer = 0

    diagonalSum1 = 0
    diagonalSum2 = 0

    for i in range(100):
        rowSum1 = 0
        colSum2 = 0
        for j in range(100):
            rowSum1 += li[i][j]
            colSum2 += li[j][i]
        answer = max(answer, rowSum1, colSum2)

    for i in range(100):
        diagonalSum1 += li[i][i]
        diagonalSum2 += li[99-i][i]

    answer = max(answer, diagonalSum1, diagonalSum2)

    print(f'#{T} {answer}')