def printEven(s):
    l = len(s)
    output = ""
    for i in range (0, l, 2):
        output += s[i]

    return output

def printOdd(s):
    l = len(s)
    output = ""
    for i in range (1, l, 2):
        output += s[i]

    return output


t = int(input())

for i in range (0, t):
    s = input()
    print(printEven(s) + " " + printOdd(s))


