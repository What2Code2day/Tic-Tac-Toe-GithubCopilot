# Make a program that allows 2 people to play a game of tic-tac-toe.

def play_game():
    print("Welcome to the game")
    print("1. Play game")
    print("2. Exit")
    choice = input("Choice: ")
    if choice == "1":
        print("Game started")
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        game_on = True
        turn = "X"
        count = 0
        while game_on:
            if turn == "X":
                print("It's X's turn")
                position = input("Choose a position from 1-9: ")
                position = int(position) - 1
                if board[position] == "-":
                    board[position] = "X"
                    count += 1
                else:
                    print("You can't go there")
                    continue
                print_board(board)
                if win_check("X", board):
                    print("X wins!")
                    game_on = False
                elif count == 9:
                    print("Tie game")
                    game_on = False
                else:
                    turn = "O"
            else:
                print("It's O's turn")
                position = input("Choose a position from 1-9: ")
                position = int(position) - 1
                if board[position] == "-":
                    board[position] = "O"
                    count += 1
                else:
                    print("You can't go there")
                    continue
                print_board(board)
                if win_check("O", board):
                    print("O wins!")
                    game_on = False
                elif count == 9:
                    print("Tie game")
                    game_on = False
                else:
                    turn = "X"
    elif choice == "2":
        print("Exiting game")
    else:
        print("Invalid choice")
        play_game()
def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def win_check(player, board):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False
play_game()
