def heightCheck(height, secondMax):
	result = height - secondMax
	if result < 0:
		return 0
	else:
		return result
for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    res = 0
    for bd in range(2, N-2):
        tmp=buildings[bd-2:bd+3]
        tmp.remove(buildings[bd])
        secondMax = max(tmp)
        res += heightCheck(buildings[bd], secondMax)
    print(f'#{tc} {res}')