import pymorphy2


morph = pymorphy2.MorphAnalyzer()

word = input()
word = morph.parse(word)[0]
ptag = word.tag.POS
words = {
    ('past', 'Прошедшее время:'): [
        {'masc'}, {'femn'}, {'neut'}, {'plur'}
    ],
    ('pres', 'Настоящее время:'): [
        {'1per', 'sing'},
        {'1per', 'plur'},
        {'2per', 'sing'},
        {'2per', 'plur'},
        {'3per', 'sing'},
        {'3per', 'plur'}
    ]
}
if ptag in {'INFN','VERB'}:
    for key, val in words.items():
        print(key[1])
        for cases in val:
            cases.add(key[0])
            wrd = word.inflect(cases).word
            print(wrd)
else:
    print('Не глагол')