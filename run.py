#!/usr/bin/env python
# Tic-Tac-Toe

# ["x", "o", "x"]
# ["x", "o", "x"]
# ["x", "x", "x"]
import random
import sys

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# map the numbers from the dummy board to the actual coordinates of the "board"
board_mapping = {1: [0, 0],
                 2: [0, 1],
                 3: [0, 2],
                 4: [1, 0],
                 5: [1, 1],
                 6: [1, 2],
                 7: [2, 0],
                 8: [2, 1],
                 9: [2, 2]
                 }


################################################
# https://stackoverflow.com/a/3041990/12075722
################################################
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


########################
# return the board
########################
def show_board(this_board):
    for i in range(len(this_board)):
        for j in range(len(this_board)):
            print(this_board[i][j]),
            if j == 2:
                print("")


########################
# pick a place to move
########################
def where_to_move(this_piece, this_board):
    global ai
    move_ok = False
    while not move_ok:
        show_board(this_board)
        if ai:
            # pick a random move from the available moves
            if len(get_possible_moves(this_board)) > 8:
                move_here = random.choice(get_possible_moves(this_board))
            else:
                move_here = minimax(this_board, random.choice(get_possible_moves(this_board)), piece, 3)[0]
            print("AI moves the piece {} to {}".format(piece, move_here))
            this_board[board_mapping[move_here][0]][board_mapping[move_here][1]] = piece
            move_ok = True
        else:
            move_here = raw_input("Where do you want to place your piece {}? ".format(this_piece))
            print("===========================")
            # is the chosen number in the board?
            if move_here.isdigit() and any(int(move_here) in k for k in this_board):
                this_board[board_mapping[int(move_here)][0]][board_mapping[int(move_here)][1]] = piece
                move_ok = True
            else:
                print("Illegal move!")


##########################
# return opponent's piece
##########################
def opponent(flip):
    return "o" if flip == "x" else "x"


########################
# MiniMax algorithm
########################
def minimax(this_board, this_move, this_piece, depth):
    best_score = 0
    best_move = this_move

    if depth == 0 or check_win(this_board)[0] == "WIN" or not get_possible_moves(this_board):
        if check_win(this_board)[1] == piece:
            score = 100
            print(check_win(this_board), piece)
        elif check_win(this_board)[1] == opponent(piece):
            score = 101
            print(check_win(this_board), piece)
        else:
            print("this is the bottom")
            show_board(this_board)
            score = 10 / (len(get_possible_moves(this_board)) + 1)
        return [this_move, score]

    for move in get_possible_moves(this_board):
        # test this move
        this_board[board_mapping[move][0]][board_mapping[move][1]] = this_piece
        curr_move, score = minimax(this_board, move, opponent(this_piece), depth - 1)
        print("Score", score, "best score", best_score, "and move", move, "and best_move", best_move, "piece", piece)
        show_board(this_board)
        best_score = max(score, best_score)
        if best_score == score:
            best_move = curr_move
        # revert the move tested above
        this_board[board_mapping[move][0]][board_mapping[move][1]] = move
    return [best_move, best_score]


########################
# get possible moves
########################
def get_possible_moves(this_board):
    k = []
    for i in range(1, 10):
        if any(i in j for j in this_board):
            k.append(i)
    return k


########################
# switch players
########################
def switch_player(this_piece):
    global ai
    if ai:
        ai = False
    else:
        ai = True
    if this_piece == "x":
        this_piece = "o"
    else:
        this_piece = "x"
    return this_piece


########################
# check if player won
########################
def check_win(this_board):
    # horizontal and vertical checks
    for x in range(len(this_board)):
        if this_board[x][0] == this_board[x][1] == this_board[x][2]:
            return "WIN", this_board[x][0]
        if this_board[0][x] == this_board[1][x] == this_board[2][x]:
            return "WIN", this_board[0][x]
    # diagonals checks
    x = 0
    if this_board[x][x] == this_board[x+1][x+1] == this_board[x+2][x+2]:
        return "WIN", this_board[x][x]
    if this_board[x][x+2] == this_board[x+1][x+1] == this_board[x+2][x]:
        return "WIN", this_board[x][x+2]
    # if we have the board full
    if not get_possible_moves(this_board):
        return "DRAW", 0
    return 0, 0


########################
# main code
########################
win = False
if query_yes_no("Wanna start first?"):
    piece = "x"
    ai = False
else:
    piece = "o"
    ai = True

first_round = True
while not win:
    # check if AI starts
    if ai and first_round:
        piece = switch_player(piece)
        ai = True
        where_to_move(piece, board)
        piece = switch_player(piece)
    first_round = False
    where_to_move(piece, board)
    if check_win(board)[0] == "WIN":
        show_board(board)
        print("Player {} WON!".format(check_win(board)[1]))
        win = True
    elif check_win(board)[0] == "DRAW":
        show_board(board)
        print("DRAW!")
        win = True
    piece = switch_player(piece)
