board = [[7, 2, 3],
         [4, 7, 4],
         [7, 5, 7]]


def check_win():
    for x in range(len(board)):
        if board[x][0] == board[x][1] == board[x][2]:
            return True
        if board[0][x] == board[1][x] == board[2][x]:
            return True
    x = 0
    if board[x][x] == board[x+1][x+1] == board[x+2][x+2]:
        return True
    if board[x][x+2] == board[x+1][x+1] == board[x+2][x-2]:
        return True


if check_win():
    print("Won")
else:
    print("Fail")
