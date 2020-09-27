import random

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break # gives a way to exit the program if you cannot guess the number
    if guess == answer:
        print("Congrats nigga!")
        break
    else:
        print("wrong")
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("You have not guessed correctly")
