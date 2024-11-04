for test_case in range(1, 11):
	T = int(input())
	N, M = map(int, input().split())
	res = pow(N, M)
	print(f"#{T} {res}")