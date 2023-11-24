list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

low = 0
high = len(list) - 1
guess = 9

while low <= high:
    mid = (low + high) // 2
    if guess == list[mid]:
        print(mid)
        break
    elif guess > list[mid]:
        low = mid + 1
    elif guess < list[mid]:
        high = mid - 1
