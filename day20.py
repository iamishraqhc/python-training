n = int(input())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            numSwaps += 1
            a[j+1], a[j] = a[j], a[j+1]

    if numSwaps == 0:
        break


print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))