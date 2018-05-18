from random import randint


def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    total = 0
    for i in word:
        total = total + score[i.lower()]
    return total


def main():
    consonants = "bcdfghjklmnpqrstvuxyz"
    vowels = "aeiou"
    vowelsNumber = randint(1, 2)
    consonantsNumber = 7 - vowelsNumber
    chosen = []
    for i in range(vowelsNumber):
        chosen.append(vowels[randint(0, 4)])
    for i in range(consonantsNumber):
        chosen.append(consonants[randint(0, 20)])
    print "Your chosen letters are " + str(",".join(chosen))
    valid = True
    index = 0
    words = open("words.txt", "r").readlines()
    while valid:
        guess = raw_input("Create a word with your chosen letters: ")
        valid2 = True
        for i in guess:
            while valid2:
                if i not in chosen:
                    print "That is not a valid guess. Enter something only uses your chosen letters and is a word."
                    valid = True
                    valid2 = False
                elif guess + "\n" in words:
                    if i == max(guess):
                        print "That is a valid word!"
                        print "The score for that word is", scrabble_score(guess)
                        valid = False
                        valid2 = False
        index += 1


main()
