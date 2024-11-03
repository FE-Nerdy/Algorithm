T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    d = {2:0, 3:0, 5:0, 7:0, 11:0}
    
    for num in d.keys():
        while(N%num == 0):
            d[num]+=1
            N //= num
    print(f'#{test_case} {" ".join(map(str,list(d.values())))}')