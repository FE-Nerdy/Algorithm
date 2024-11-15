T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    answer = 1

    #체크
    for i in range(9):
        colList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rowList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if sudoku[i][j] in colList:
                colList.remove(sudoku[i][j])
            else :
                answer = 0
                break
            if sudoku[j][i] in rowList:
                rowList.remove(sudoku[j][i])
            else :
                answer = 0
                break
        if len(colList) != 0 or len(rowList) != 0:
            answer = 0
            break
    #격자 체크
    for i in range(3):
        for j in range(3):
            gridList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for col in range(3):
                for row in range(3):
                    if sudoku[i*3+col][j*3+row] in gridList:
                        gridList.remove(sudoku[i*3+col][j*3+row])
                    else:
                        answer = 0
                        break
            if len(gridList) != 0:
                answer = 0
                break


    print(f'#{tc} {answer}')
