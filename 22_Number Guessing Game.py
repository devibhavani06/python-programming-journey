import random
secret=random.randint(1,10)
guess=int(input("Guess a number between 1 and 10: "))
if guess==secret:
    print("You Won!")
else:
    print("You Lost!")
    print("The number was",secret)
