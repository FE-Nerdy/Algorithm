for tc in range(1, 11):
    dump = int(input())
    Nlist = list(map(int, input().split()))

    for x in range(dump):
        Nlist.sort()
        Nlist[0] += 1
        Nlist[-1] -= 1
    print(f"#{tc} {max(Nlist)-min(Nlist)}")