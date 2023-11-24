import sys

ak = []
data = list(map(str.strip, sys.stdin))
lis = data[0].split()
for el in data:
    if el == data[0]:
        break
    else:
        el = el.split(',')
        for i in range(len(lis)):
            if el[2] == lis[i]:
                ak.append(f'{el[1]} ({el[3]})')
print(ak)