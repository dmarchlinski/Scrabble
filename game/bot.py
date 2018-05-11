import re

def make_list():
    english = []
    print "1 - 50k dictionary database"
    answer = raw_input("2 - 500k dictionary database:")
    if answer == "1":
        with open("words.txt") as fd:
            english = fd.readlines()
    elif answer == "2":
        with open("words2.txt") as fd:
            english = fd.readlines()

    for i in range(len(english)):
        english[i] = english[i][:-1]

    english = map(str.lower, english)

    return english


def main():
    english = make_list()
    repeat = True

    while repeat == True:
        string = raw_input("enter phrase: ")
        string = re.sub("[^a-zA-z]", "", string)
        string = string.lower()

        letters = []
        eng_word = []
        counter = 0
        word_count = 0
        large = []

        for j in string:
            letters.append(j)

        for ind_word in english:
            for i in ind_word:
                eng_word.append(i)

            count = 0
            length = len(eng_word)

            for i in letters:
                if any(i in j for j in eng_word):
                    eng_word.remove(i)
                    counter = counter + 1

                if counter == length:
                    large.append(ind_word)
                    print ind_word  # delete "#" if u want all words printed
                    word_count = word_count + 1
                    break

            counter = 0
            loop = True

            del eng_word[:]

        if any(string in s for s in large):
            large.remove(string)

        let_count = 0
        large_list = []
        for word in large:
            if len(word) > let_count:
                large_list = [word]
                let_count = len(word)
            elif len(word) == let_count:
                large_list.append(word)

        print " "
        print "there are", word_count, "possible words you can make"
        print "the largest word(s):", large_list
        # print large           


main()
