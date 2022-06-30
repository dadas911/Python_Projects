import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winning_moves = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
player_score = 0
computer_score = 0

def print_score():
    print("Player -", player_score, " : ", computer_score,"- Computer")

def reset_board():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_board():
    display = '\n '

    for x in range(9):
        if (x%3) == 0 and x != 0:
            display += '\n-----------\n '
        elif x != 0:
            display += ' | '

        
        display +=  board[x]
    
    display += '\n'
    print(display)
        
def generate_move():
    while True:
        computer_move = random.randint(0, 8)
        if board[computer_move] == ' ':
            return computer_move

def is_win():
    for line in winning_moves:
        if (board[line[0]] == board[line[1]] == board[line[2]] 
            and (board[line[0]] == 'X' or board[line[0]] == 'O')):
            return True
    return False


def start_game():
    global board
    global computer_score
    global player_score
    
    print('\033[1m' + "\nWelcome to tic-tac-toe game, you have 'X'.\n" + '\033[0m')
    print_board()

    while True:
        # Users turn
        user_input = int(input("Enter number (1-9): ")) - 1
        # Check input logic
        if board[user_input] == ' ':
            board[user_input] = 'X'
        else:
            continue
        print_board()

        if is_win():
            print("You won!\n")
            player_score += 1
            break

        # Computers turn - generate random move
        computer_move = generate_move()
        board[computer_move] = 'O'
        print("Computer generated:", computer_move + 1)
        print_board()

        if is_win():
            print("You lost!\n")
            computer_score += 1
            break

    print_score()
    again = input("Do you want to play again (Y/N)? ")
    if again == "Y":
        start_game()
    else:
        print("Thank you for playing\n")
    
if __name__ == '__main__':
    start_game()