x = 0
score = 0

def start_game():
    start_answer = ''
    while start_answer != 'Y':
        start_answer = input('Are you ready to start, Y/N? ')
        if start_answer == 'N':
            print('Wrong Answer!')
        else:
            print('Please answer with Y or N')
    print("Let's Begin! ")
    x = int(input('Choose a range for the number you would like to guess: '))
    game(x)
    play_again = input('Would you like to play again, Y/N? ')
    while play_again == "Y":
        game(x)
    print('Thanks for playing! Your score: ' + str(score))
        

def game(x):
    import random
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input('Pick a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Try Again. Too Low.')
        elif guess > random_number:
            print('Sorry, Try Again. Too High')
    print('CONGRATS! You guessed correctly!')
    score + 1



start_game()