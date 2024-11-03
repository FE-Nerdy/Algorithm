T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    res = 0
    if N % 2 == 0:
        res -= N*(2+N)//4
        res += N*(N)//4
    else :
        res -= (N-1)*(1+N)//4
        res += (N+1)*(N+1)//4
    print(f'#{test_case} {res}')