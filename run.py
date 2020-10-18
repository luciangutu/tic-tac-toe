#!/usr/bin/env python
# Tic-Tac-Toe

# ["x", "o", "x"]
# ["x", "o", "x"]
# ["x", "x", "x"]
import random
import sys

dummy_board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

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

moves = 9

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
    for p in this_board:
        print(p)


########################
# pick a place to move
########################
def where_to_move(this_piece):
    global ai, moves
    move_ok = False
    while not move_ok:
        show_board(board)
        if ai:
            number = random.randint(1, 9)
            print("AI moves the piece {} to {}".format(piece, number))
            # is the chosen number in the board?
            if any(number in k for k in board):
                board[board_mapping[number][0]][board_mapping[number][1]] = piece
                move_ok = True
                moves -= 1
            else:
                print("Illegal move!")
        else:
            move_here = raw_input("Where do you want to place your piece {}? ".format(this_piece))
            # is the chosen number in the board?
            if move_here.isdigit() and any(int(move_here) in k for k in board):
                board[board_mapping[int(move_here)][0]][board_mapping[int(move_here)][1]] = piece
                move_ok = True
                moves -= 1
            else:
                print("Illegal move!")


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
def check_win():
    # horizontal and vertical checks
    for x in range(len(board)):
        if board[x][0] == board[x][1] == board[x][2]:
            return True
        if board[0][x] == board[1][x] == board[2][x]:
            return True
    # diagonals checks
    x = 0
    if board[x][x] == board[x+1][x+1] == board[x+2][x+2]:
        return True
    if board[x][x+2] == board[x+1][x+1] == board[x+2][x]:
        return True
    # if we have the board full
    # this can be replaced with nested for loops anc check if each board piece is not x or o
    if moves <= 0:
        show_board(board)
        print("DRAW!")
        exit(0)


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
        where_to_move(piece)
        piece = switch_player(piece)
    first_round = False
    where_to_move(piece)
    if check_win():
        show_board(board)
        print("Player {} WON!".format(piece))
        win = True
    piece = switch_player(piece)


