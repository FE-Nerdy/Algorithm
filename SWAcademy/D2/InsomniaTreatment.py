T = int(input())
for test_case in range(1, T + 1):
	N = int(input())
	cnt = 1
	li = []

	while len(li) < 10:
		for n in list(map(int, str(cnt*N))):
			if n not in li:
				li.append(n)
		cnt+=1
	print(f"#{test_case} {N*(cnt-1)}")