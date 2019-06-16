################################
##########  CREDITS ############
#   TEAM: Connect 4            #
#   Guan Hao Wu | 0976154      #
#   Gizem Sazak | 0965662      #
#   Bilal Azrioual | 0966189   #
################################
################################

import numpy as np
import visual_v1 as vs

# Initialize program
running = True

# DEFINES
ROW_COUNTER = 6
COLUMN_COUNTER = 7


# who's turn? player 1 or 2
turn = 0
# remained moves available
remained_moves = 42

# if clicked on close, stop loop
gameover = False
win = False
text = ''


# color defining
RED = (255, 0, 0)
YELLOW = (0, 255, 255)
BLUE = (0, 0, 255)


# Defining Functions
# Create the board in arrays per row. 6 row 7 column
def create_board():
    board = np.zeros((ROW_COUNTER, COLUMN_COUNTER))
    return board


# Draw board
def draw_board():
    bord = vs.bord()
    return print(bord)


# flip numpy lists vertically
def print_board(board):
    print(np.flip(board, 0))


# get board value each slot and give correct color.
def board_value_slot():
    row = 0
    while row < ROW_COUNTER:
        col = 0
        while col < COLUMN_COUNTER:
            num = board[row][col]
            vs.tile_color(int(num), row, col)
            col += 1
        row += 1


# Get empty slot in row per column
def get_empty_slot(board, column):
    for row in range(ROW_COUNTER):
        if board[row][column] == 0:
            return row


# Checks if there are at least 1 empty slot in the chosen column.
def valid_slot(board,col):
    if board[5][col] == 0:
        return True


def drop_coin_action(board, col, player):
    row = get_empty_slot(board, col)
    drop_coin(board, row, col, player)


# Change List value to player value
def drop_coin(board, row, col, player):
    board[row][col] = player


# removes 1 available moves from total moves available.
def rmv(turn, moves):
    turn += 1
    moves -= 1
    return turn, moves


# Check for win
def winning_algorithm(board, piece):
    # Horizontal
    for c in range(COLUMN_COUNTER - 3):
        for r in range(ROW_COUNTER):
            if board[r][c] == piece and board[r][c+1] == piece and \
                    board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Vertical
    for c in range(COLUMN_COUNTER):
        for r in range(ROW_COUNTER - 3):
            if board[r][c] == piece and board[r+1][c] == piece and \
                    board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Diagonal positive
    for c in range(COLUMN_COUNTER - 3):
        for r in range(ROW_COUNTER - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and \
                    board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Diagonal negative
    for c in range(COLUMN_COUNTER - 3):
        for r in range(3, ROW_COUNTER):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and \
                    board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


# function to execute playerChoice and drop coin if valid slot in column.
def player_turn(board, turn, moves, pcc, text):
    player = turn+1
    col = pcc-1
    if valid_slot(board, col):
        drop_coin_action(board, col, player)
        turn, moves = rmv(turn, moves)
        return turn, moves, text
    else:
        text = 'Not a valid move! Try again.'
    return turn, moves, text


board = create_board()
# print_board(board)
draw_board()
board_value_slot()
vs.update_screen()


# infinite loop to keep display running
# Game going-on
while running:
    while not gameover and remained_moves > 0:
        mx, my = vs.get_mouse()
        vs.get_event(gameover)
        moves = remained_moves
        t = turn % 2
        player = t + 1
        vs.zwartbalk()
        vs.turn(player, mx)
        playerinput = ""
        playerinput = input("Player " + str(player) + ", Make your choice (1-7): ")
        while (len(playerinput)<1 or int(playerinput)>7 or int(playerinput) == 0):
            playerinput = input("Player " + str(player) + ", Make your choice (1-7): ")
        
        playerChoiceColumn = int(playerinput)
        turn, remained_moves, text = player_turn(board, t, moves, playerChoiceColumn, text)
        win = winning_algorithm(board, player)
        board_value_slot()
        print_board(board)
        if win:
            text = 'Player ' + str(player) + ' win!'
            win = False
            gameover = True
        if not win and remained_moves == 0:
            text = 'DRAW'
            gameover = True
        vs.display_msg(player, text)
        vs.update_screen()
        text = ''
    vs.get_event(gameover)
