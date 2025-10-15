import random

def validate_input(user_guess):
    if not user_guess.isdigit():
        print('Invalid input. Please enter a number.')
        return False

    num = int(user_guess)
    if num < 1 or num > 100:
        print('Invalid input. Please enter a number between 1 and 100.')
        return False

    return True

def play_round():
    rand_num = random.randint(1, 100)
    print('\nI chose a number between 1 and 100. Try to guess it!')
    score = 100

    while True:
        user_guess = input('Guess a number between 1 and 100 (or q to quit): ')
        if user_guess.lower() == 'q':
            print('You quit this round. The number was', rand_num)
            return 0   # return 0 if the player quits

        if not validate_input(user_guess):
            continue

        guess = int(user_guess)

        if guess < rand_num:
            print('Your guess is too low. Try again.')
            score = max(score - 10, 0)
        elif guess > rand_num:
            print('Your guess is too high. Try again.')
            score = max(score - 10, 0)
        else:
            print(f'Congratulations! You guessed the correct number.\nYour score is {score}')
            return score   # ✅ return final score

def start_game():
    print('Welcome to the Guessing Game!')
    while True:
        final_score = play_round()        # now gets a proper integer
        print(f'Round finished. Score: {final_score}')
        again = input('Do you want to play again? (yes/no): ').strip().lower()
        if again not in ('yes', 'y'):
            print('Thanks for playing! Goodbye.')
            break

if __name__ == '__main__':
    start_game()
