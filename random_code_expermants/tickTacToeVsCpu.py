import random

board = [' ' for x in range(10)]


def insert_to_position(mark, place):
    """
    | place a new mark on the board
    :param mark: mark to place
    :param place: the position to fill
    """
    board[place] = mark


def free_space(position):
    """
    | check if the given position if empty
    :param position: the position to check
    :return: True when the position is free
    """
    return board[position] == ' '


def print_board():
    """
    | print the game board
    """
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[1]} | {board[2]} | {board[3]}\n")


def is_winner(bo, mark):
    """
    | check if any winning condition is meet
    :param bo: the board to check
    :param mark: the mark to check if won
    :return: True when a condition is meet
    """
    # 1st 3 bool for win with a row
    # 2nd 3 bool for win in a column
    # last 2 bool for win in a diagonal
    return (bo[7] == bo[8] == bo[9] == mark) or (bo[4] == bo[5] == bo[6] == mark) or \
           (bo[1] == bo[2] == bo[3] == mark) or \
           (bo[1] == bo[4] == bo[7] == mark) or (bo[2] == bo[5] == bo[8] == mark) or \
           (bo[3] == bo[6] == bo[9] == mark) or \
           (bo[7] == bo[5] == bo[3] == mark) or (bo[1] == bo[5] == bo[9] == mark)


def player_move():
    """
    | get the move the player want to make
    :return: the index to fill with the player's move
    """
    while True:
        move = input('Where do you want to place \'X\'? (1-9)\n')
        try:
            move = int(move)
            if move in range(0, 10):
                if free_space(move):
                    return move
                print('This spot is taken')
            else:
                raise ValueError
        except ValueError:
            print('I don\'t understand your input')


def comp_move():
    """
    | make the computer pick a move to play
    :return: index to fill a move . 0 when out of moves
    """
    available_moves = [x for x, mark in enumerate(board) if (mark == ' ' and x != 0)]
    # look for a move to win with then look to block the player
    for mark in ['O', 'X']:
        for i in available_moves:
            copy = board[:]
            copy[i] = mark
            if is_winner(copy, mark):
                return i

    # pick random place from the free spaces
    open_corner = []
    for i in available_moves:
        if i in [1, 3, 7, 9]:
            open_corner.append(i)
    if len(open_corner) > 0:
        return random_pick(open_corner)

    if 5 in available_moves:
        return 5
    open_edge = []

    for i in available_moves:
        if i in [2, 4, 6, 8]:
            open_edge.append(i)
    if len(open_edge) > 0:
        return random_pick(open_edge)
    return 0


def random_pick(li):
    """
    | pick a random number in a list
    :param li: the list to pick from
    :return: the value was picked
    """
    length = len(li)
    index = random.randrange(0, length)
    return li[index]


def is_full(bo):
    """
    | check if the game board is full
    :param bo: the board to check
    :return: True when full, False otherwise
    """
    if bo.count(' ') > 1:
        return False
    return True


def main():
    """
    | the main game control and move order
    """
    print_board()
    while not (is_full(board)):
        # when the cpu haven't won the player move
        if not is_winner(board, 'O'):
            move = player_move()
            insert_to_position('X', move)
            print_board()
        else:
            print('CPU win, good luck next time')
            break
        # when the player haven't won the cpu move
        if not is_winner(board, 'X'):
            move = comp_move()
            if move == 0:
                # when the cpu cant move it's a tie
                print('It\'s a tie')
            else:
                insert_to_position('O', move)
                print(f"Cpu placed \'O\' in position {move}")
                print_board()
        else:
            print("You Won! Well played!")
            break


if __name__ == '__main__':
    main()
