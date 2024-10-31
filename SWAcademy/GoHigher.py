def findMaxFloor(N, P):
    maxHeight = N * (N + 1) // 2
    dp = [False] * (maxHeight + 1)
    dp[0] = True

    # DP
    for i in range(1, N + 1):
        for j in range(maxHeight, i - 1, -1):
            if dp[j - i] and j != P:
                dp[j] = True

    # 가장 높은 층 찾기
    for floor in range(maxHeight, -1, -1):
        if dp[floor]:
            return floor
    return 0

test_case = int(input())
for _ in range(test_case):
    N, P = map(int, input().split())
    print(findMaxFloor(N, P))