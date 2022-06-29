import random

highscore = 0

def start_game():
    rand_num = random.randint(1,99)
    print('\033[1m' + '\nRandom number from range <1,99> was generated\n' + '\033[0m')
    print(rand_num)
    curr_score = 0

    while True:
        user_guess = int(input("Enter your guess (0 if you want to exit): "))
        curr_score += 1

        # User inputted 0 -> exit program
        if user_guess == 0:
            exit()

        # User guessed correctly -> print winning message and break while loop
        if user_guess == rand_num:
            print("\nCorrect, you won!\n")
            break
        elif user_guess < rand_num:
            print("Unknown number is bigger.\n")
        else:
            print("Unknown number is smaller.\n")
    
    global highscore
    if (curr_score < highscore) or (highscore == 0):
        highscore = curr_score
        print("New highscore:", highscore)

    answer = input("Do you want to play again (Y/N)? ")
    if(answer == "Y"):
        start_game()
    else:
        print("Thanks for playing. Your highscore:", highscore, "\n")



if __name__ == '__main__':
    start_game()