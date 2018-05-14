def main():

    board_letters = [["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"],["a","b","c","d","e","f","g","h","i","j"]]
    boardui = []
    for i in range(10):
        boardui.append([])
        for j in range(10):
            boardui[i].append("[ "+str(board_letters[i][j])+" ]")
    for i in boardui:
        print i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+"\n"

    del boardui[:]


main()
