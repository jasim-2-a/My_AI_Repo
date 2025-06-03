import random
print("Let's Guess the Number")
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess!=random_number):
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess<random_number:
            print("Try again. Your guess is too low: ")
        elif (guess>random_number):
            print("Try again. Your number is too high: ")
        else:
            print("Congratulations! you  guess the correct number ")

guess(100)
