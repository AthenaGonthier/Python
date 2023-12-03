

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

guesses = []
print(random.randint(1, 100))
cpu_num = random.randint(1, 100)
player_num = int(input("Enter a number between 1-100:"))

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too high!")
    else:
        print("Too low!")
    player_num = int(input("Enter a number between 1-100: "))
    guesses.append(player_num)

else:
    print("Well done!!")
    print("it took you %i guesses." % len(guesses))
    print("Here are your guesses:")
    print(guesses)
