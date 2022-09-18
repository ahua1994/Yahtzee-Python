from random import random
from tabulate import tabulate
import math

finished = []


def main():
    table = [["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "3 of a\nKind",
                          "4 of a\nKind", "Full\nHouse", "Small\nStraight", "Large\nStraight", "Yahtzee", "Chance"], ["Current\nScore", *[0]*13], ["Score\nTo Add", *[0]*13]]
    # score_table(table)
    dice = roll()
    print(dice, draw_dice(dice))


def roll():
    dice = []
    for _ in range(5):
        dice.append(math.ceil(random() * 6))
    return dice


def reroll():
    pass


def draw_dice(list):
    d6 = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    return [d6[i-1] for i in list]


def add_score(table):
    pass


def score_table(table):
    # table for all 3 rows, table[:2] for first 2 rows

    print(tabulate(table[:2], tablefmt="grid"))


if __name__ == "__main__":
    main()
