T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    scoreList = list(map(int,input().split()))
    ansList = [0 for _ in range(101)]
    
    for score in scoreList:
        ansList[score-1] += 1
    ans = max(list(filter(lambda x: ansList[x]==max(ansList),range(len(ansList)))))
    print(f'#{N} {ans+1}')