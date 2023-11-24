word1 = input()
word2 = input()
yes = 'да'
no = 'нет'
if word1 == yes or word1 == no:
    if word1 == no or word1 == yes:
        if word2 == yes or word2 == no:
            if word2 == no or word2 == yes:
                print('ВЕРНО')
            else:
                print('НЕВЕРНО')
        else:
            print('НЕВЕРНО')
    else:
        print('НЕВЕРНО')
else:
    print('НЕВЕРНО')