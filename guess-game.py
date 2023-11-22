import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input('Pick a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Try Again. Too Low.')
        elif guess > random_number:
            print('Sorry, Try Again. Too High')
    print('CONGRATS! You guessed correctly!')

guess(10)
