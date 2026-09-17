import random
num = random.randint(1,100)

tries = 0

while True:
    guessed = int(input("Guess the number between 1 to 100: "))
    tries += 1

    if guessed == num:
        print("Congratulations you guess right number.")
        break

    elif guessed > num:
        print("You need go lower.")

    elif guessed < num:
        print("You need go upper.")

print(f"You guess your number in {tries} of tries.")