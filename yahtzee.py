from random import random
from tabulate import tabulate
import math


def main():
    table = [["Section", "1's", "2's", "3's", "4's", "5's", "6's", "3 of a\nKind",
              "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
             ["Current\nScore", *[0]*13], ["Score\nTo Add", *[0]*13], ["Finished", *[False]*13]]
    game(table)


def roll():
    dice = []
    for _ in range(5):
        dice.append(math.ceil(random() * 6))
    return dice


def reroll(dice):
    rolls = 1
    again = None
    select = None
    while rolls <= 3:
        print("Roll " + str(rolls))
        while again not in ["y", "n", "yes", "no"]:
            again = input("Do you want to reroll? Y/N: ").lower()
        if again == "y" or again == "yes":
            valid = False
            while valid == False:
                select = input(
                    "Select Dice Slot(s) to Reroll.\nExample: 1 2 3 4 5 \n").split(" ")
                for i in range(len(select)):
                    try:
                        if isinstance(int(select[i]), int) and int(select[i]) > 0 and int(select[i]) < 7:
                            select[i] = int(select[i]) - 1
                            valid = True
                        else:
                            print(
                                "Please Enter Dice Slot Number(s) Seperated by a Space.")
                            valid = False
                            break
                    except (ValueError):
                        print(
                            "Please Enter Dice Slot Number(s) Seperated by a Space.")
                        valid = False
                        break
            for i in set(select):
                dice[i] = math.ceil(random() * 6)
            draw_dice(dice)
            again = None
            rolls += 1
        else:
            break
    return dice


def draw_dice(list):
    d6 = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    print([d6[i-1] for i in list])


def add_score(table):
    pass


def score_table(table):
    # table for all 3 rows, table[:2] for first 2 rows

    print(tabulate(table, tablefmt="grid"))


def game(table):
    turn = 1
    while turn <= 13:
        print("Turn " + str(turn))
        score_table(table[:2])
        dice = roll()
        draw_dice(dice)
        dice = reroll(dice)
        add_score(table)
        turn += 1


if __name__ == "__main__":
    main()
