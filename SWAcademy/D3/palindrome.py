def palindrome_check(word):
    cv = True
    times = len(word) // 2
    for i in range(times):
        if word[i] != word[-(1+i)]:
            cv = False
    return cv

for tc in range(1, 11):
    N = int(input())
    charList = [list(input()) for _ in range(8)]
    cnt = 0

    #가로 탐색
    for y in range(8):
        for x in range(9-N):
            word = ""
            for k in range(N):
                word += charList[y][x+k]
            if palindrome_check(word): cnt+=1

    #세로 탐색
    for y in range(9-N):
        for x in range(8):
            word = ""
            for k in range(N):
                word += charList[y+k][x]
            if palindrome_check(word): cnt+=1
    print(f'#{tc} {cnt}')