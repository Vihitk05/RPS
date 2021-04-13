# random function
import random

# 4 variables choices & scores of Human & Computer
computer_score = 0
human_score = 0
human_choice = 0
computer_choice = 0
rps_dict = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}


# Input function for Human & Computer
def inputs_of_human_and_computer():
    global human_choice
    global computer_choice
    while True:
        try:
            human_choice = int(input('Enter your choice [0: Rock,1: Paper,2: Scissors]: '))
            if human_choice == 0 or human_choice == 1 or human_choice == 2:
                computer_choice = random.randint(0, 2)
                print(f'Human Choice: {human_choice}')
                print(f'Computer Choice: {computer_choice}')
                return human_choice,computer_choice
            else:
                print('Enter a number between 0,1,2!')
        except ValueError:
            print('Enter a Valid Choice!')
            print('[0: Rock,1: Paper,2: Scissors]')


# Play game
def play_rps():
    while True:
        global computer_choice
        global human_choice
        global human_score
        global computer_score
        global rps_dict
        inputs_of_human_and_computer()

        print(f'Your Choice: {rps_dict.get(human_choice)}')
        print(f'Computer Choice: {rps_dict[computer_choice]}')

        if (human_choice - computer_choice) % 3 == 1:
            print('You win this turn!')
            human_score += 1
            print(f'Your score: {human_score}')
            print(f'Computer score: {computer_score}')
            print('\n' * 10)
            if human_score == 3:
                print('You won this round!')
                replay()
                break
        elif human_choice == computer_choice:
            print('Tie!')
            print(f'Your score: {human_score}')
            print(f'Computer score: {computer_score}')
            print('\n' * 10)
        else:
            computer_score += 1
            print('Computer wins this turn!')
            print(f'Your score: {human_score}')
            print(f'Computer score: {computer_score}')
            print('\n' * 10)
            if computer_score == 3:
                print('Computer wins this round!')
                replay()
                break


# Replay the game
def replay():
    global computer_score
    global human_score
    while True:
        human = input('Do you want to play again [Y/N]? ').upper()
        if human == 'Y':
            computer_score = 0
            human_score = 0
            play_rps()
            return human_score, computer_score
        else:
            print('Thank you!')
            break


# Enjoy the game bud!
play_rps()
