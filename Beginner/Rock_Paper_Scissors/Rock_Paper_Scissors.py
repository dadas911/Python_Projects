import random

score_player = 0
score_computer = 0

def print_score():
    print("\nPlayer:", score_player, "\nComputer:", score_computer,"\n")

def start_game():
    possible_choices = ["R", "P", "S"]
    global score_player
    global score_computer

    while True:
        # Let user pick his choice
        player_choice = input("Enter your choice - [R]ock, [P]aper, [S]cissors or [E]xit: ")
        # Generate random choice for computer
        computer_choice = random.choice(possible_choices)

        if player_choice == "E":
            print("Thank you for playing.")
            print_score()
            exit()

        print("You played:", player_choice)
        print("Computer played:", computer_choice,"\n")
                
        # Same choices -> Draw
        if player_choice == computer_choice:
            print("Draw!")
            score_computer += 1
            score_player += 1
        # Player played Rock
        elif player_choice == "R":
            if computer_choice == "P":
                print("You lost!")
                score_computer += 1
            elif computer_choice == "S":
                print("You won!")
                score_player += 1
        # Player played Paper
        elif player_choice == "P":
            if computer_choice == "R":
                print("You won!")
                score_player += 1
            elif computer_choice == "S":
                print("You lost!")
                score_computer += 1
        # Player player Scissors
        elif player_choice == "S":
            if computer_choice == "R":
                print("You lost!")
                score_computer += 1
            elif computer_choice == "P":
                print("You won!")
                score_player += 1
        else:
            print("Invalid choice!")

        print_score()

    

if __name__ == '__main__':
    start_game()