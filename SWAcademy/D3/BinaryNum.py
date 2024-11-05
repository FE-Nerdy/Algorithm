T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    binaryNum = format(M, 'b')
    res = binaryNum[-N:]
    ans = "OFF"
    
    if res == "1"*N: ans = "ON"
    print(f'#{test_case} {ans}')