arr = []
for i in range(6):
    arr_temp = list(map(int, input().split(' ')))
    arr.append(arr_temp)

maxi = 0

for i in range(0, 4):
    sum = 0
    for j in range(0, 4):

        sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if i==0 and j==0:
            maxi = sum
        if sum > maxi:
            maxi =sum

print(maxi)