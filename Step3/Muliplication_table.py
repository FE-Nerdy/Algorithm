N = int(input())

if ( 1 <= N <= 9 ) :
    for i in range(1, 10) :
        print("%d * %d = %d" %(N, i, N*i))