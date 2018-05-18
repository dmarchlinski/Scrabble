import random
def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    vowels = "AEIOU"
    board_letters = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "S", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "C", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "R", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "R", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "A", "P", "P", "L", "E", " "],
                     [" ", " ", " ", " ", "B", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "L", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", "E", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    running = True
    hand = []
    for i in range(5):
        hand.append(random.choice(alphabet))
    for i in range(2):
        hand.append(random.choice(vowels))

    while running:

        boardui = []
        for x in range(10):
            boardui.append([])
            for y in range(10):
                boardui[x].append("[ " + str(board_letters[x][y]) + " ]")

        print "     1    2    3    4    5    6    7    8    9    10  \n"
        horizontal = "abcdefghij"
        count = 0
        for i in boardui:
            print horizontal[count] + "  " + i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + i[9] + "  " + \
                  horizontal[count] + "\n"
            count = count + 1
        print "     1    2    3    4    5    6    7    8    9    10  "
        print
        print "Hand: "+hand[0]+" "+hand[1]+" "+hand[2]+" "+hand[3]+" "+hand[4]+" "+hand[5]+" "+hand[6]
        print "\n\n"

        good_len = True
        while good_len:

            row1 = raw_input("row of first letter: ")
            row1 = int(chr(int((ord(row1)) - 49)))
            column1 = input("column of first letter: ")
            column1 = column1 - 1

            row2 = raw_input("row of second letter: ")
            row2 = int(chr(int((ord(row2)) - 49)))
            column2 = input("column of second letter: ")
            column2 = column2 - 1

            word = raw_input("enter word using letters in hand: ")


            if column1 == column2:

                if row1 > row2:  # bottom to top
                    if len(word) <= row1 + 1:
                        good_len = False
                    else:
                        print "does not fit on board"

                if row2 > row1:  # top to bottom
                    if len(word) <= 10 - row1:
                        good_len = False
                    else:
                        print "does not fit on board"

            if row1 == row2:

                if column1 > column2:  # right to left
                    if len(word) <= column1 + 1:
                        good_len = False
                    else:
                        print "does not fit on board"

                if column2 > column1:  # left to right
                    if len(word) <= 10 - column1:
                        good_len = False
                    else:
                        print "does not fit on board"

        word = word.upper()

        for i in range(len(word)):
            if column1 == column2:
                if row1 > row2:
                    board_letters[row1 - i][column1] = word[i] #printing bottom to top
                if row1 < row2:
                    board_letters[row1 + i][column1] = word[i] #printing top to bottom
            if row1 == row2:
                if column1 > column2:
                    board_letters[row1][column1 - i] = word[i] #printing right to left
                if column1 < column2:
                    board_letters[row1][column1 + i] = word[i] #printing left to right

        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" #clears page for new board print
main()
