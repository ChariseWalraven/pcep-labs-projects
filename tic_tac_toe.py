from random import randrange

board = [
    [i+1+(3*j) for i in range(3)] for j in range(3)
]

# get a list of tuples representing the value of the cell, the column, and the row
indices = [(i+1+(3*j), i, j) for j in range(3) for i in range(3)]


def formatting():
    border = ('+-------')*3+'+'
    blank_line = '|       '*3+'|'
    cell_separator = '|'
    cell_spacing = '   '
    return (border, blank_line, cell_separator, cell_spacing)


def compose_board(formatting, board):
    (border, blank_line, c_sep, c_space) = formatting()
    disp = border
    for row in board:
        disp += '\n' + blank_line + '\n' + c_sep
        for cell in row:
            disp += c_space + str(cell) + c_space + c_sep
        disp += '\n' + blank_line + '\n' + border
    return disp


def update_board(board, move, is_computer=False):
    # find the correct cell
    # update the cell with the correct symbol
    (val, col_index, row_index) = list(
        filter(lambda z: z[0] == move, indices))[0]
    row = board[row_index]
    cell = row[col_index]
    symbol = 'X' if is_computer else 'O'
    board[row_index][col_index] = symbol


def invalid_input_error(messsage='Please enter the number of the cell.', notify=True):
    if notify:
        print('Input invalid.', messsage)


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(compose_board(formatting, board))


def get_user_input(attempt=0) -> int:
    move = -1
    if 4 > attempt > 2:
        print('Last attempt. One more incorrect input will result in disqualification.')

    try:
        move = int(input('Enter your move:'))
    except Exception as e:
        if attempt >= 3:
            invalid_input_error('You\'re disqualified.')
            return move
        invalid_input_error()
        get_user_input(attempt+1)
    return move


def move_is_valid(move, notify=True):
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


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move = get_user_input()
    if move == -1:
        return False
    while not move_is_valid(move):
        move = get_user_input()
        if move == -1:
            return False
    else:
        update_board(board, move)
    return True


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
    # check diagonals
    # if symbol present, return cell value
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
        # get all columns
        col = []
        for row in bin_cells:
            col.append(row[i])
        # check columns
        if col == [1, 1, 1]:
            return True
        cols.append(col)

    diagonals = [diagonal1, diagonal2]
    if [1, 1, 1] in diagonals:
        return True


def draw_move(board):
    # The function draws the computer's move and updates the board.
    # get random move
    move = randrange(1, 10)
    # check if move valid
    while not move_is_valid(move,notify=False):
        move = randrange(1, 10)
    else:
        # update board
        print(f'Computer chose {move}.')
        update_board(board, move, is_computer=True)


def game():
    print('Computer moves first...')
    update_board(board, 5, is_computer=True)
    while True:
        display_board(board)
        if not enter_move(board):
            print('Computer wins. 🤖')
            break
        if victory_for(board, 'O'):
            print('You win! 🎉')
            break
        display_board(board)
        draw_move(board)
        if victory_for(board, 'X'):
            print('Computer wins! 🤖')
            break


# main program
game()

# testing
