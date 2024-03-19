#prompt for integer =>1
#create a random number between that and 0
#prompt user to guess the random number
#say more, less, or just right
import random
userint = None

while True:
    try: 
        userint = int(input("Give me a number >0: "))
    except Exception:
        print("Input was not a valid number")
        continue

    if userint >= 1:
        break
    else:
        print("Number not an integer >0")

programguess = random.randint(1,userint)
print(programguess)

while True:
    try: 
        userguess = int(input(f"From 1 to {userint}, what number am I thinking of?: "))
    except Exception:
        print("Guess must be an integer")
        continue #skips rest of loop and restarts loop

    if userguess == programguess:
        print("You're right!")
    elif userguess < programguess:
        print("Too low!")
    elif userguess > programguess:
        print("Too high!")
        break