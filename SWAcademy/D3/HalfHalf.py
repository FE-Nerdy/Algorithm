T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	S = list(input())
	dic = {}
	ans = 'Yes'
	for i in range(4):
		if S[i] not in dic: dic[S[i]] = 1
		else: dic[S[i]] += 1
	for values in dic.values():
		if values != 2: ans = 'No'
	if len(dic) != 2: ans = 'No'
	print(f'#{test_case} {ans}')