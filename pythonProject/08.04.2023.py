n = int(input())
for i in range(n):
    string = input()
    if len(string) > 10:
        string = string[0] + str((len(string) - 2)) + string[-1]
    print(string)
