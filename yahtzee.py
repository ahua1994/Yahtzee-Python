from random import random
from tabulate import tabulate
from collections import Counter
import math


def main():
    table = [["Section", "1's", "2's", "3's", "4's", "5's", "6's", "3 of a\nKind",
              "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
             ["Current\nScore", *[0]*13], ["Score\nTo Add", *[0]*13], ["Completed", *["No"]*13]]
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
        print("\nRoll " + str(rolls) + "\n")
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


def add_score(table, dice):
    sorted = dice.sort()
    for i in range(1, 14):
        if i <= 6:
            for j in range(5):
                if dice[j] == i:
                    table[2][i] += dice[j]
        elif i == 7 or i == 8:
            for j in range(1, 7):
                if dice.count(j) >= i-4:
                    table[2][i] += sum(dice)
        elif i == 9:
            if len(Counter(dice).keys) == 2:
                table[2][i] += 25
        elif i == 10:
            pass
        elif i == 11:
            pass
    return table


def score_table(table):
    # table for all 3 rows, table[:2] for first 2 rows

    print(tabulate(table, tablefmt="grid"))


def game(table):
    turn = 1
    while turn <= 13:
        print("Turn " + str(turn))
        score_table(table)
        dice = roll()
        draw_dice(dice)
        dice = reroll(dice)
        table = add_score(table, dice)
        score_table(table)
        print("why")
        turn += 1


if __name__ == "__main__":
    main()
