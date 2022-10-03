from random import random
from tabulate import tabulate
from collections import Counter
import math


def main():
    table = [["Section", "1's", "2's", "3's", "4's", "5's", "6's", "3 of a\nKind",
              "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
             ["Current\nScore", *[0]*13], ["Score\nTo Add",
                                           *[0]*13], ["Completed", *["No"]*13],
             ["Bonus + Joker", 0], ["Total Score", 0]]
    game(table)


def reroll(table):
    dice = []
    for _ in range(5):
        dice.append(math.ceil(random() * 6))
    rolls = 1
    again = None
    select = None
    while rolls <= 3:
        table = roll_score(table, dice)
        score_table(table)
        print(tabulate([["Roll " + str(rolls)]], tablefmt="grid"))
        draw_dice(dice)
        if rolls == 3:
            return table
        while again not in ["y", "n", "yes", "no"]:
            again = input("\nDo you want to reroll? Y/N: ").lower()
        if again == "y" or again == "yes":
            table[2] = ["Score\nTo Add", *[0]*13]
            valid = False
            while valid == False:
                select = input(
                    "\nSelect Dice Slot(s) to Reroll.\nExample: 1 2 3 4 5 \n").split(" ")
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
    return table


def draw_dice(list):
    d6 = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    print(tabulate([[d6[i-1] for i in list]], tablefmt="grid"))


def roll_score(table, dice):
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
            rollValues = list(Counter(dice).values())
            if rollValues == [2, 3] or rollValues == [3, 2]:
                table[2][i] += 25
        elif i == 10:
            smstr1 = [1, 2, 3, 4]
            smstr2 = [2, 3, 4, 5]
            smstr3 = [3, 4, 5, 6]
            if any([all(num in dice for num in smstr1),
                    all(num in dice for num in smstr2),
                    all(num in dice for num in smstr3)]):
                table[2][i] += 30
            pass
        elif i == 11:
            sorted = [*dice]
            sorted.sort()
            if sorted == [1, 2, 3, 4, 5] or sorted == [2, 3, 4, 5, 6]:
                table[2][i] += 40
        elif i == 12:
            if len(set(dice)) == 1:
                table[2][i] += 50 if table[3][i] == "No" else 100
        else:
            table[2][i] += sum(dice)
    return table


def score_table(table):
    # table for all 3 rows, table[:2] for first 2 rows

    print(tabulate(table[:4], tablefmt="grid"))
    print(tabulate(table[4:6], tablefmt="grid"))


def game(table):
    turn = 1
    while turn <= 13:
        print(tabulate([["Turn " + str(turn)]], tablefmt="grid"))
        table = reroll(table)
        table = add_score(table)
        table[2] = ["Score\nTo Add", *[0]*13]
        print(table[1][1:7], "hi")
        table[4][1] = 35 if sum(table[1][1:7]) >= 63 else 0
        table[5][1] = sum(table[1][1:]) + table[4][1]
        # score_table(table)
        turn += 1
    print("Game Over! Your Final Score is " + str(table[5][1]))


def add_score(table):
    section = None
    categories = ["Section", "1's", "2's", "3's", "4's", "5's", "6's", "3 of a Kind",
                  "4 of a Kind", "Full House", "Small Str8", "Large Str8", "Yahtzee", "Chance"]
    while (section not in categories[1:]):
        print(categories[1:])
        section = input("Enter a Valid Category: ").strip()
        try:
            if table[3][categories.index(section)] == "Yes":
                print("\nThis Section Has Been Completed\n")
                section = None
                continue
        except:
            print("Invalid Input")
            continue
    index = categories.index(section)
    table[1][index] += table[2][index]
    table[3][index] = "Yes"
    return table
# Add 2nd and 3rd yahtzee 100 automatically
# Joker rules?


if __name__ == "__main__":
    main()
