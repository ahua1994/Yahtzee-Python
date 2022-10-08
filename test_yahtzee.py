from yahtzee import draw_dice, roll_score, bonus
from tabulate import tabulate


# d6 = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


def main():
    test_draw_dice()
    test_roll_score()
    test_bonus()


def test_draw_dice():
    assert draw_dice([5, 5, 5, 5, 5]) == tabulate(
        [["⚄", "⚄", "⚄", "⚄", "⚄"]], tablefmt="grid")
    assert draw_dice([1, 2, 3, 4, 5]) == tabulate(
        [["⚀", "⚁", "⚂", "⚃", "⚄"]], tablefmt="grid")
    assert draw_dice([3, 2, 3, 6, 1]) == tabulate(
        [["⚂", "⚁", "⚂", "⚅", "⚀"]], tablefmt="grid")


def test_roll_score():
    table = [["Section", "1's", "2's", "3's", "4's", "5's", "6's", "3 of a\nKind",
              "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
             ["Current\nScore", *[0]*13], ["Score\nTo Add",
                                           *[0]*13], ["Completed", *["No"]*13],
             ["63 to Bonus", 0], ["Total Score", 0]]
    test_dice_1 = [6, 6, 6, 6, 6]
    test_dice_2 = [5, 4, 3, 2, 1]
    test_dice_3 = [4, 2, 6, 1, 3]
    assert roll_score(table, test_dice_1)[2] == [
        "Score\nTo Add", *[0]*5, 30, 30, 30, 0, 0, 0, 50, 30]
    table[2] = ["Score\nTo Add", *[0]*13]
    assert roll_score(table, test_dice_2)[2] == [
        "Score\nTo Add", 1, 2, 3, 4, 5, 0, 0, 0, 0, 30, 40, 0, 15]
    table[2] = ["Score\nTo Add", *[0]*13]
    assert roll_score(table, test_dice_3)[2] == [
        "Score\nTo Add", 1, 2, 3, 4, 0, 6, 0, 0, 0, 30, 0, 0, 16]


def test_bonus():
    table = [["Section", "1's", "2's", "3's", "4's", "5's", "6's", "3 of a\nKind",
              "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
             ["Current\nScore", *[0]*13], ["Score\nTo Add",
                                           *[0]*13], ["Completed", *["No"]*13],
             ["63 to Bonus", 0], ["Total Score", 0]]
    test_dice = [1, 4, 3, 4, 4]
    test_dice_1 = [4, 4, 4, 4, 4]
    test_dice_2 = [5, 5, 5, 5, 5]
    test_dice_3 = [6, 6, 6, 6, 6]

    assert bonus(table, test_dice)[1] == ["Current\nScore", *[0]*13]
    table[1] = ["Current\nScore", *[0]*11, 50, 0]
    table[3] = ["Completed", *["No"]*11, "Yes", "No"]
    assert bonus(table, test_dice_1)[1] == ["Current\nScore", *[0]*11, 150, 0]
    assert bonus(table, test_dice_2)[1] == ["Current\nScore", *[0]*11, 250, 0]
    assert bonus(table, test_dice_3)[1] == ["Current\nScore", *[0]*11, 350, 0]


if __name__ == "__main__":
    main()
