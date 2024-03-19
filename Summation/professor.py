import random

def main():
    i=0
    k=0
    score = 0
    level = get_level()

    while i < 10:
        i += 1
        x = generate_integer(level)
        y = generate_integer(level)

        while k < 3:
            k += 1
            answer = int(input(f"what is {x} + {y}?: "))

            if answer == x+y:
                print("Correct!")
                score += 1
                k=0
                break
            elif k == 3:
                print(f"Answer is {x+y}")
            else:
                print("EEE")

    print(f"After 10 problems, your score is {score}.")

def get_level():
    while True:
        try: 
            level = int(input("Choose a level from 1, 2, 3: "))
            if 1<=level<=3:
                return level
        except Exception:
            pass

def generate_integer(level):
    lower = 10 ** (level-1)
    upper = 10 ** level - 1 
    return random.randint(lower, upper)


if __name__ == "__main__":
    main()