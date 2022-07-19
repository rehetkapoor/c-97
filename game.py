import random
print("Number Guessing Game")

number=random.randint(1,9)
chances=0
print("Guess a Number from 1-9")

while chances<5:
    guess=int(input("Enter your Guess= "))
    if guess==number:
        print("Congrats, you won!")
        break
    elif guess<number:
        print("Too Low, Guess Higher Than", guess)
    else:
        print("Too High, Guess Lower Than", guess)
    chances+=1
if not chances<5:
    print("You Lose. The number was: ", number)

