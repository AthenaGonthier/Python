# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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
