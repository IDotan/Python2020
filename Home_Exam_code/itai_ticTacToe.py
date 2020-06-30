"""
simple code of a tic tac to game in python console
"""
game_board = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in game_board:
    board_keys.append(key)


def print_board(board):
    """
    | print the game bored on the screen
    :param board: the bord to print
    """
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('---------')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('---------')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


def check_winning_condition(bord):
    """
    | check if any winning condition was met
    :param bord: the game bord
    :return: True when a condition was met
    """
    if game_board['7'] == game_board['8'] == game_board['9'] != ' ':
        print_board(game_board)
        return True
    elif game_board['4'] == game_board['5'] == game_board['6'] != ' ':
        print_board(game_board)
        return True
    elif game_board['1'] == game_board['2'] == game_board['3'] != ' ':
        print_board(game_board)
        return True
    elif game_board['1'] == game_board['4'] == game_board['7'] != ' ':
        print_board(game_board)
        return True
    elif game_board['2'] == game_board['5'] == game_board['8'] != ' ':
        print_board(game_board)
        return True
    elif game_board['3'] == game_board['6'] == game_board['9'] != ' ':
        print_board(game_board)
        return True
    elif game_board['7'] == game_board['5'] == game_board['3'] != ' ':
        print_board(game_board)
        return True
    elif game_board['1'] == game_board['5'] == game_board['9'] != ' ':
        print_board(game_board)
        return True
    return False


def play_again():
    """
    | ask if to start a new game at the end of the last
    """
    while True:
        restart = input("Do you want to play Again?(y/n)\n")
        if restart.lower() == "y" or restart == "yes":
            for key in board_keys:
                game_board[key] = " "
            game(player1, player2)
        if restart.lower() == "n" or restart == "no":
            exit()
        print("I don't understand your input")
        continue


def get_move():
    """
    | get the next move of the player
    :return: the move to make
    """
    while True:
        try:
            move = input()
            if int(move) in range(1, 10):
                return move
            else:
                raise ValueError
        except ValueError:
            print("only 1-9 are valid input")


def game(player1, player2):
    """
    | the tic tack toe game
    :param player1: name of player 1
    :param player2: name of player 2
    """
    turn = player1
    symbol = 'X'
    count = 0
    for i in range(10):
        print("use the NumPad to place marker on the board.")
        print_board(game_board)
        print(f"It's your turn, {turn}. Place {symbol} in which place?")
        move = get_move()
        if game_board[move] == ' ':
            game_board[move] = symbol
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        # check if any wining condition is meet at the end of a turn, after the 5th turn
        if count >= 5:
            if check_winning_condition(game_board):
                print("\nGame Over.\n")
                print(f" **** {turn} won. ****")
                break
        # when no wining condition is meet and at the last move
        if count == 9:
            print_board(game_board)
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break
        # switch the player and the symbol
        if turn == str(player1):
            turn = player2
            symbol = 'O'
        else:
            turn = player1
            symbol = 'X'
    play_again()


def get_name(num):
    """
    | get the name of the player
    :param num: num of the player
    :return: the player name
    """
    while True:
        player = input(f"player {num} enter your name:\n")
        if player == "":
            print("cant stay empty")
            continue
        return player


if __name__ == "__main__":
    player1 = get_name(1)
    player2 = get_name(2)
    game(player1, player2)
