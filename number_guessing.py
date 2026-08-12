import random
num = random.randint(1, 100)
s = 1
try:
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != num:
        if guess < num:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Guess again: "))
        s = s + 1
        if guess == num:
            print("Congratulations! You guessed the number:", num)
            print("It took you", s, "guesses.")
            break
        if s > 7:
            print("Sorry, you've used all your guesses. The number was:", num)
            break
        
        
except ValueError:
    print("Invalid input! Please enter a valid integer.")