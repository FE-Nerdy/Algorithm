N = int(input())

arr = list(map(int, input().split()))
min = arr[0]
max = arr[0]

for i in arr[1:] :
    if i < min :
        min = i
    if i > max :
        max = i

print(min, max)