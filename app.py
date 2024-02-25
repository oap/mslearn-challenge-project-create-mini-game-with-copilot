import random
# welcome user to play the game
print('Welcome to the Rock, Paper, Scissors game!')

# a list of game options, rock, paper, or scissors
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
game_options = ['rock', 'paper', 'scissors']
user_score = 0
total_rounds = 0

# create a function that will play the game
def play_game():
    '''
    This function will play the game
    '''
    user_score = 0
    # get the user's choice, warn if it's not a valid choice
    user_choice = input('Enter rock, paper, or scissors: ')
    user_choice = user_choice.lower()
    if user_choice not in game_options:
        print('Invalid choice')
        exit()
    # get the computer's choice
    computer_choice = random.choice(game_options)

    # print the user's choice and the computer's choice
    print('You chose:', user_choice)
    print('The computer chose:', computer_choice)

    # determine the winner, count user score if user wins
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        user_score += 1
        print('You win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        user_score += 1
        print('You win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        user_score += 1
        print('You win!')
    else:
        print('You lose!')
    return user_score

# create a loop that and ask the user continue to play or not
while True:
    user_score += play_game()
    total_rounds += 1
    user_continue = input('Do you want to play again? (yes/no): ')
    if user_continue == 'no':
        break

# print the user's score
print(f'Your score: {user_score} / {total_rounds}')