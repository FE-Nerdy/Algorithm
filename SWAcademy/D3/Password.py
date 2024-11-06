for tc in range(10):
	N, password = input().split()
	ans = []

	for i in password:
		if not ans or ans[-1] != i:
			ans.append(i)
		else:
			ans.pop()

	a = ''.join(ans)
	print(f'#{tc+1} {a}')