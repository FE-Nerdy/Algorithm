T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, str(input())))
    CV = 0
    ans = 0
    for i in range(len(N)):
        if N[i] != CV:
            if CV == 0:
                CV+=1
            else:
                CV-=1
            ans+=1
    print(f'#{test_case} {ans}')