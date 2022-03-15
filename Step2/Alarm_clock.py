H, M = map(int, input().split())

if ((0 <= H <= 23) and (0 <= M <= 60)) :
    if ( M < 45 ) :
        if( H == 0 ) :
            print("23 %d" %(M+15))
        else :
            print("%d %d" %(H-1, M+15))
    else :
        print("%d %d" %(H, M-45))