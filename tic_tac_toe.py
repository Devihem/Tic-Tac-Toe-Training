"""
Project: Tic-Tac-Toe in Terminal
File: tic_tac_toe.py
Author: Ivaylo Stoyanov - Devihem

This is a basic project in python for the game Tic-Tac-Toe.
The idea of this the project is to be done with procedure programing without hardcoded indexes.There are some additional
stuff added like custom board size , custom players size , gaming board visualisation in terminal and option for new
game. For better experience all inputs are handled to stay repetitive until a proper input is received.

Players take turns placing their tokens on the board by selecting coordinates in format Row:Col .
If a player has a row, column, or diagonal filled with his symbol the player wins.
If no player wins and the board is full, the game is considered a draw.

"""


def select_grid_size():
    while True:
        try:
            grid_size = int(input("Please select Grid Size:\n-> "))

            if grid_size < 3:
                raise ValueError

        except ValueError:
            print("Incorrect input! [Expected integer with value 3 or bigger]\n\n")
            continue

        return grid_size


def select_players_number():
    while True:
        try:
            players_number = int(input("Please select how many players will participate:\n-> "))

            if players_number < 2:
                raise ValueError

        except ValueError:
            print("Incorrect input! [Expected integer with value 2 or bigger]\n\n")
            continue

        return players_number


def select_players_symbol(players_count):
    players_list = []

    for player_numb in range(players_count):

        while True:
            try:
                player_symbol = input(f"Player {player_numb + 1}, please select your symbol:\n-> ")

                if player_symbol in players_list or len(player_symbol) != 1:
                    raise ValueError

                players_list.append(player_symbol)

                break

            except ValueError:
                print("Incorrect input! [Expected single Symbol that is not already in use from another player]\n\n")
                continue

    return tuple(players_list)


def playing_phase(board, players, grid_size):
    max_moves = grid_size ** 2
    made_moves = 0

    while True:

        for player in players:
            row, col = place_symbol_on_board(board, grid_size, player)
            board[row][col] = player
            made_moves += 1
            winner_flag = winner_check(board, grid_size)

            if winner_flag:
                return (f"\n\n--------- We have a winner !---------\n"
                        f"     Player with symbol " + "\033[32m" + f"{player}" + "\033[0m" + " WIN !\n\n")

            elif max_moves == made_moves:
                return ("\n\nNo more moves."
                        "\nGame is DRAW !\n\n")


def winner_check(board, grid_size):
    winner_flag = False

    # Rows - Check

    for row in range(grid_size):
        for col in range(grid_size - 1):
            current_symbol = board[row][col]
            next_symbol = board[row][col + 1]
            if current_symbol == '' or current_symbol != next_symbol:
                break
        else:
            winner_flag = True

    # Columns - Check
    for col in range(grid_size):
        for row in range(grid_size - 1):
            current_symbol = board[row][col]
            next_symbol = board[row + 1][col]
            if current_symbol == '' or current_symbol != next_symbol:
                break
        else:
            winner_flag = True

    # Primer diagonal - Check
    for row in range(grid_size - 1):
        col = row
        current_symbol = board[row][col]
        next_symbol = board[row + 1][col + 1]
        if current_symbol == '' or current_symbol != next_symbol:
            break
    else:
        winner_flag = True

    # Secondary diagonal - Check
    for row in range(grid_size - 1, 0, -1):
        col = grid_size - 1 - row
        current_symbol = board[row][col]
        next_symbol = board[row - 1][col + 1]
        if current_symbol == '' or current_symbol != next_symbol:
            break
    else:
        winner_flag = True

    return winner_flag


def place_symbol_on_board(board, grid_size, player):
    board_print(board, grid_size)
    while True:

        try:
            player_pick_location = input(
                f"Select where you want to place your Token "
                f"[" + "\033[32m" + f"{player}" + "\033[0m" + "] in format Row:Col !\n -> ").split(":")

            if len(player_pick_location) != 2:
                raise ValueError

            for loc in player_pick_location:
                for el in loc:
                    if not el.isdigit():
                        raise ValueError

            row = int(player_pick_location[0])
            col = int(player_pick_location[1])

            if 0 < row <= grid_size and 0 < col <= grid_size:
                row = row - 1
                col = col - 1
            else:
                raise ValueError

            if gaming_board[row][col] != "":
                raise ValueError

            return row, col

        except ValueError:
            print("Incorrect input! [Expected valid coordinates in format Row:Col where the block is free !]\n\n")
            continue


def another_game_select():
    while True:
        try:
            new_game = input("\n\nDo you want to play another game ? [Y/N]:\n -> ")

            if new_game.upper() not in ['Y', 'N']:
                raise ValueError

            if new_game.upper() == 'Y':
                return True

            return False

        except ValueError:
            print("Incorrect input! [Expected Y or N]\n\n")
            continue


# --------------------------------------------------PRINTS-------------------------------------------------------------
def welcome_text():
    print("\n\n"
          "\n---------------------------------Welcome-to-my-mini-project----------------------------------"
          "\n   ______    ____   ______         ______    ___      ______         ______   ____     ______"
          "\n  /_  __/   /  _/  / ____/        /_  __/   /   |    / ____/        /_  __/  / __ \\   / ____/"
          "\n   / /      / /   / /              / /     / /| |   / /              / /    / / / /  / __/   "
          "\n  / /     _/ /   / /___           / /     / ___ |  / /___           / /    / /_/ /  / /___   "
          "\n /_/     /___/   \\____/          /_/     /_/  |_|  \\____/          /_/     \\____/  /_____/  "
          "\n----------------------------------------------------------------------------------------------"
          "\n\n")


def board_print(board, grid_size):
    list_with_indexes_top = ['']

    for numb in range(grid_size):
        str_numb = str(numb + 1)
        str_numb = ' ' * (4 - len(str_numb)) + str_numb

        list_with_indexes_top.append(str_numb)

    # Top frame
    print('┌──' + '──┬──' * grid_size + '──┐')

    # Index Top
    print('│    ' + '│'.join(list_with_indexes_top) + '│')

    # Mid Rows
    counter = 0
    for row in board:
        counter += 1
        str_counter = str(counter)
        str_counter = ' ' * (4 - len(str_counter)) + str_counter
        print_row = [' ' * (4 - len(el)) + el for el in row]
        print('├──' + '──┼──' * grid_size + '──┤')
        print('│' + '│'.join([str_counter] + print_row) + '│')

    # Bottom frame
    print('└──' + '──┴──' * grid_size + '──┘\n')


# -------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    welcome_text()

    SIZE_OF_GRID = select_grid_size()

    NUMBER_OF_PLAYERS = select_players_number()

    while True:

        gaming_board = [['' for _ in range(SIZE_OF_GRID)] for __ in range(SIZE_OF_GRID)]

        players_order_and_symbols = select_players_symbol(NUMBER_OF_PLAYERS)

        print(playing_phase(gaming_board, players_order_and_symbols, SIZE_OF_GRID))

        if not another_game_select():
            break

    print("Thank you for playing !")

# input from somewhere ?!?
# Change winner check  with all()
# Class 1 board class 2 players
