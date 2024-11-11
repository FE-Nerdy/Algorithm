def posCheck(n):
    for i in range(n):
        if row[n] == row[i] or abs(row[n] - row[i]) == abs(n - i):
            return False
    return True

def dfs(n) :
    global ans
    if n == N :
        ans += 1
        return
    else:
        for i in range(N):
            row[n] = i
            if posCheck(n):
                dfs(n+1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    row = [0] * N
    ans = 0
    dfs(0)
    
    print(f"#{test_case} {ans}")