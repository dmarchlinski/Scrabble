import random
import os


def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10, "_": 0}
    total = 0
    for i in word:
        total = total + score[i.lower()]
    return total


def main():
    alphabet = "BCDFGHJKLMNPQRSTVQXYZ"
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

        if len(hand) < 7:
            for i in range(7-(len(hand))):

                hand.append(random.choice(alphabet))
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
            word = raw_input("Create a word with your chosen letters: ")
            word = word.upper()
            # valid = True
            # index = 0
            # words = open("words.txt", "r").readlines()
            # while valid:
            #     word = raw_input("Create a word with your chosen letters: ")
            #     valid2 = True
            #     for i in word:
            #         while valid2:
            #             #print i.upper()
            #             #print hand
            #             if i.upper() not in hand:
            #                 if word + "\n" not in words:
            #                     print "That is not a valid word. Enter something only uses your chosen letters and is a word."
            #                     valid = True
            #                 valid2 = False
            #             elif i == max(word):
            #                 print "That is a valid word!"
            #                 print "The score for that word is: ", scrabble_score(word)
            #                 valid = False
            #                 valid2 = False
            #             else:
            #                 valid2 = False
            #                 valid = False
            #     index += 1


            exist_letters = []
            for i in board_letters:
                for j in i:
                    if j != " ":
                        exist_letters.append(j)
            hand_temp = hand[:]
            count_hand = 0
            connecting = False
            if column1 == column2:

                if row1 > row2:  # bottom to top
                    if len(word) <= row1 + 1:
                        for i in range(len(word)):
                            if board_letters[row1 - i][column1] == word[i]:
                                hand_temp.append(word[i])
                                connecting = True
                            if word[i] in hand_temp:
                                count_hand = count_hand + 1
                                hand_temp.remove(word[i])
                            else:
                                print "invalid letter(s)"
                                count_hand = 0
                            if count_hand == len(word):
                                if connecting == True:
                                    for i in range(len(word)):
                                        board_letters[row1 - i][column1] = word[i]
                                else:
                                    print "connect word to existing letter on board"
                    else:
                        print "does not fit on board"

                if row2 > row1:  # top to bottom
                    if len(word) <= 10 - row1:
                        for i in range(len(word)):
                            if board_letters[row1 + i][column1] == word[i]:
                                 hand_temp.append(word[i])
                                 connecting = True
                            if word[i] in hand_temp:
                                 count_hand = count_hand + 1
                                 hand_temp.remove(word[i])
                            else:
                                 print "invalid letter(s)"
                                 count_hand = 0
                            if count_hand == len(word):
                                if connecting == True:
                                    for i in range(len(word)):
                                        board_letters[row1 + i][column1] = word[i]
                    else:
                        print "does not fit on board"

            if row1 == row2:

                if column1 > column2:  # right to left
                    if len(word) <= column1 + 1:
                        for i in range(len(word)):
                            if board_letters[row1][column1 - i] == word[i]:
                                hand_temp.append(word[i])
                                connecting = True
                            if word[i] in hand_temp:
                                count_hand = count_hand + 1
                                hand_temp.remove(word[i])
                            else:
                                print "invalid letter(s)"
                                count_hand = 0
                            if count_hand == len(word):
                                if connecting == True:
                                    for i in range(len(word)):
                                        board_letters[row1][column1 - i] = word[i]
                                else:
                                    print "connect word to existing letter on board"
                    else:
                        print "does not fit on board"

                if column2 > column1:  # left to right
                    if len(word) <= 10 - column1:
                        for i in range(len(word)):
                            if board_letters[row1][column1 + i] == word[i]:
                                hand_temp.append(word[i])
                                connecting = True
                            if word[i] in hand_temp:
                                count_hand = count_hand + 1
                                hand_temp.remove(word[i])
                            else:
                                print "invalid letter(s)"
                                count_hand = 0
                            if count_hand == len(word):
                                if connecting == True:
                                    for i in range(len(word)):
                                        board_letters[row1][column1 + i] = word[i]
                                else:
                                    print "connect word to existing letter on board"
                    else:
                        print "does not fit on board"
            if count_hand == len(word):
                good_len = False
                hand = hand_temp
                del hand_temp[:]
                connecting = False



        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" #clears page for new board print or os.clear for terminal
main()
