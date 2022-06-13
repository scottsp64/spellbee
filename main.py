from english_words import english_words_lower_alpha_set

requiredLetter  = 'h'
letters = ['h','n','t','o','l','a','e']
letters = sorted(letters)
print(letters)
# letter1 = requiredLetter
# letter2 = 'n'
# letter3 = 't'
# letter4 = 'o'
# letter5 = 'l'
# letter6 = 'a'
# letter7 = 'e'

def getFinalList():
    wordlist = english_words_lower_alpha_set
    # wlcount = f'Wordlist Length: {len(wordlist)}'
    # print(wlcount)
    wordlistoffourormore = [x for x in wordlist if len(x) >= 4]
    # wlcount = f'Wordlist of four or more chars Length: {len(wordlistoffourormore)}'
    # print(wlcount)
    sortedwordlist =  (sorted(wordlistoffourormore))
    # wlcount = f'Sorted Wordlist Length: {len(sortedwordlist)}'
    # print(wlcount)
    eliminatedList = [x for x in sortedwordlist if requiredLetter not in x ]
    # wlcount = f'Wordlist Length After eliminating words without the required letter: {len(eliminatedList)}'
    # print(wlcount)
    # print(eliminatedList)
    for word in eliminatedList:
        if any(letter in word for letter in letters):
            tmpword = word
            print(tmpword)
            if any(letter in word for letter in letters):
                tmpword = tmpword
                letters.pop(0)
                print(tmpword)

            #     if any(letter in word for letter in letters):
            #         tmpword = tmpword
            #         letters.pop(0)
            #         if any(letter in word for letter in letters):
            #             tmpword = tmpword
            #             letters.pop(0)
            #             print(tmpword)
            # print(word)
        
getFinalList()


