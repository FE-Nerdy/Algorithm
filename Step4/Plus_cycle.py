import sys

n = int(sys.stdin.readline())
tmp = -1
result = 0
if( 0 <= n <= 99 ) :
    while (n != tmp) :
        tmp = n
        small = tmp % 10
        big = tmp // 10
        tmp = small * 10 + ((small + big)%10)
        result+=1

print (result)