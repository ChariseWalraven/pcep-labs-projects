import time

from random import randrange

# TODO: check file for immutability and convert as many functions as possible to pure functions
# NOTE: currently implementing FP practices -> https://www.geeksforgeeks.org/functional-programming-in-python/

def new_board():
    return [
        [i+1+(3*j) for i in range(3)] for j in range(3)
    ]


def compose_board(board, formatting):
    (border, blank_line, c_sep, c_space) = formatting()
    disp = border
    for row in board:
        disp += '\n' + blank_line + '\n' + c_sep
        for cell in row:
            disp += c_space + str(cell) + c_space + c_sep
        disp += '\n' + blank_line + '\n' + border
    return disp


def update_board(board, move, is_computer=False):
    # determine which sign to use
    sign = 'X' if is_computer else 'O'

    return list(
        map(lambda row:
            list(
                map(lambda cell:
                    sign if cell == move else cell, row
                    )
                ), board
            )
        )

# BUG: printing many lines results in the board being lost somewhere above the last line
def invalid_input_error(message='Please enter the number of the cell.', notify=True):
    if notify:
        print('Input invalid.', message)


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    def formatting():
        border = ('+-------')*3+'+'
        blank_line = '|       '*3+'|'
        cell_separator = '|'
        cell_spacing = '   '
        return (border, blank_line, cell_separator, cell_spacing)

    print(compose_board(board, formatting))


# BUG: disqualification doesn't work. Is it really necessary?
def get_user_input(attempt=0) -> int:
    move = -1
    if 4 > attempt > 2:
        print('Last attempt. One more incorrect input will result in disqualification.')
    try:
        move = int(input('Enter your move:'))
    except Exception as e:
        if attempt >= 3:
            invalid_input_error('You\'re disqualified.')
            return -1
        invalid_input_error()
        get_user_input(attempt+1)
    return move


def move_is_valid(board, move, notify=True) -> bool:
    # must be an int
    # must be an empty cell
    is_valid = False
    if type(move) != int:
        invalid_input_error('Input must be an integer.', notify)
    elif not (10 > move > 0):
        invalid_input_error(
            'You must choose a number between 1 and 9.', notify)
    elif move not in [cell for row in board for cell in row]:
        invalid_input_error('That cell is already taken', notify)
    else:
        is_valid = True
    return is_valid


def enter_move(board) -> (list, bool):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    # NOTE: there's gotta be a better way to catch disqualifications from get_user_input
    move = get_user_input()
    is_valid = True
    if move == -1:
        is_valid = False
        return (board, is_valid)
    while not move_is_valid(board, move):
        move = get_user_input()
    return (update_board(board, move), is_valid)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row_index in range(len(board)):
        for col_index, cell in enumerate(board[row_index]):
            if type(cell) == int:
                free_fields.append((row_index, col_index))
    return free_fields


def victory_for(board, sign) -> bool:
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    bin_cells = list(map(lambda row: list(
        map(lambda cell: 1 if cell == sign else 0, row)), board))

    diagonals = []
    diagonal1 = []
    diagonal2 = []
    cols = []
    if [1, 1, 1] in bin_cells:
        return True
    for i in range(len(bin_cells)):
        row = bin_cells[i]
        diagonal1.append(row[i])
        diagonal2.append(row[-i-1])
        col = []
        for row in bin_cells:
            col.append(row[i])
        if col == [1, 1, 1]:
            return True
        cols.append(col)

    diagonals = [diagonal1, diagonal2]
    if [1, 1, 1] in diagonals:
        return True


def is_draw(board):
    # check if draw
    filled_cells = map(lambda row: list(
        filter(lambda cell: type(cell) == str, row)), board)
    filled_cells = [cell for row in filled_cells for cell in row]
    return True if len(filled_cells) == 9 else False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    # get random move
    move = randrange(1, 10)
    # check if move valid
    while not move_is_valid(board, move, notify=False):
        move = randrange(1, 10)
    else:
        # update board
        print(f'Computer chose {move}.')
        return update_board(board, move, is_computer=True)


def game():
    print(f'{"="*12+" INFO "+"="*12}\nComputer is "X", player is "O"',
          end=f'\n{"="*30}\n\n')
    turn = 0
    board = new_board()
    in_play = True
    while in_play:
        turn += 1
        valid_move = True
        if turn == 1:
            # computer always moves first
            print('Computer moves first...')
            board = update_board(board, 5, is_computer=True)
        elif turn % 2 == 0:
            # player's turn
            (board, valid_move) = enter_move(board)
            if not valid_move:
                print('Computer wins. 🤖')
                in_play = False
            elif victory_for(board, 'O'):
                print('You win! 🎉')
                in_play = False
        else:
            # computer's turn
            board = draw_move(board)
            if victory_for(board, 'X'):
                print('Computer wins! 🤖')
                in_play = False
        if is_draw(board):
            print('It\'s a draw!')
            in_play = False

        display_board(board)


# main program
game()

# testing
